from django.urls import path
import io
from utilis.function import BaseListAPIView
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db import connection
from utilis.export_funtion import try_convert_date
import pandas as pd
from decimal import Decimal
from urllib.parse import quote
from django.views import View
from django.template.response import TemplateResponse as render


def export(request, type):
    return render(request, "export.html")


class exports(View):
    def post(self, request):
        post_data = request.POST.dict()
        company_id = request.session.get("company_id")
        branch_id = request.session.get("branch_id")
        status_approve = post_data.get("status_approve", "").strip()
        start_date = try_convert_date(post_data.get("start_date", ""))
        end_date = try_convert_date(post_data.get("end_date", ""))

        cursor = connection.cursor()
        try:
            query = """
                SELECT a.app_id AS "เลขที่ขออนุมัติ",
                    a.created_at AS "วันที่",
                    a.customer_name AS "ชื่อ - นามสกุลลูกค้า",
                    a.mobile AS "เบอร์โทรลูกค้า",
                    a.place_of_work AS "ประจำบริษัท",
                    a.office AS "บริษัทซัพคอนแทรค",
                    e.occup_name AS "ประเภทอาชีพ",
                    CASE 
                        WHEN a.category_occupation = '1' THEN 'รายได้คงที่'
                        WHEN a.category_occupation = '2' THEN 'รายได้ไม่สม่ำเสมอ'
                    END AS "หมวดอาชีพ",
                    COALESCE(a.price, 0) AS "ยอดขอกู้",
                    g.score_3 AS "คะแนน",
                    g.grade AS "เกรด",
                    CASE 
                        WHEN a.status_approve = '1' THEN 'ผ่าน'
                        WHEN a.status_approve = '2' THEN 'ทำสัญญาแล้ว'
                        WHEN a.status_approve = '9' THEN 'ไม่ผ่าน'
                        WHEN a.status_approve = '5' THEN 'ยกเลิก' 
                        ELSE 'รออนุมัติ' 
                    END AS "สถานะอนุมัติ",
                    a.condition_approve AS "หมายเหตุ"
                FROM View_InstallmentDetail a  
                LEFT JOIN auth_user b ON b.username = a.user_id
                LEFT JOIN tb_customerinfo c ON c.id = a.customer_id
                LEFT JOIN Tb_MasterNCB d ON d.id = a.ncb_id
                LEFT JOIN tb_masteroccupation e ON e.id = c.occupation_id
                LEFT JOIN auth_user f ON f.username = a.user_id
                LEFT JOIN tb_customerscore g ON g.installmentdetail_id = a.id
                WHERE CAST(a.created_at AS DATE) BETWEEN %s AND %s
                AND a.create_to_branch_id = %s 
                AND a.company_id = %s
            """

            params = [start_date, end_date, branch_id, company_id]

            if status_approve.lower() != "all":
                query += " AND COALESCE(a.status_approve, 0) = %s"
                params.append(status_approve)

            query += " ORDER BY a.created_at"

            # print("query: ", query % tuple(["'%s'" % p for p in params]))
            cursor.execute(query, params)

            columns_header = [col[0] for col in cursor.description]
            row_data = [dict(zip(columns_header, row)) for row in cursor.fetchall()]
        finally:
            cursor.close()

        return export_xlsx("รายงานการขออนุมัติสินเชื่อ.xlsx", row_data, None)


def export_xlsx(filename, data, rename_column=None):
    df = pd.DataFrame.from_records(data)
    get_col_type = []
    if data:
        first_row = data[0]
        for key, value in first_row.items():
            index = list(first_row).index(key)
            get_col_type.append(
                {
                    "key": key,
                    "type": type(value),
                    "index": index,
                }
            )

    if get_col_type:
        for foo in get_col_type:
            if foo["type"] == Decimal:
                df[foo["key"]] = pd.to_numeric(df[foo["key"]])

    if rename_column:
        df.rename(columns=rename_column, inplace=True)

    output = io.BytesIO()

    with pd.ExcelWriter(
        output,
        engine="xlsxwriter",
        date_format="dd/mm/yyyy",
        datetime_format="dd/mm/yyyy",
    ) as writer:
        df.to_excel(writer, sheet_name="Sheet1", index=False)

        workbook = writer.book
        worksheet = writer.sheets["Sheet1"]

        currency_format = workbook.add_format({"num_format": "#,##0.00"})

        for foo in get_col_type:
            if foo["type"] == Decimal:
                worksheet.set_column(foo["index"], foo["index"], 20, currency_format)

    output.seek(0)

    response = HttpResponse(
        output.getvalue(),
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response["Content-Disposition"] = "attachment; filename*=UTF-8''%s" % quote(
        filename
    )

    return response
