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
        branch_id = request.session.get("branch_id") 
        print("branch_id :", branch_id)
        status_approve = post_data.get("status_approve", "") 
        print("status_approve :", status_approve)
        start_date = try_convert_date(post_data.get("start_date", ""))
        print("start_date :", start_date)
        end_date = try_convert_date(post_data.get("end_date", ""))
        print("end_date :", end_date)
        
        print('params 5555',[start_date,end_date,status_approve,branch_id])
        
        cursor = connection.cursor()
        try:
            query = """
                SELECT a.app_id AS "เลขที่ขออนุมัติ",
                    a.created_at AS "วันที่",
                    a.customer_name AS "ชื่อ - นามสกุลลูกค้า",
                    a.mobile AS "เบอร์โทรลูกค้า",
                    a.refer_name AS "ชื่ออ้างอิง 1",
                    a.refer_description AS "เกี่ยวข้องเป็น",
                    a.refer_telephone AS "เบอร์โทรอ้างอิง 1",
                    a.refer_name2 AS "ชื่ออ้างอิง 2",
                    a.refer_description2 AS "เกี่ยวข้องเป็น",
                    a.refer_telephone2 AS "เบอร์โทรอ้างอิง 2",
                    a.refer_name3 AS "ชื่ออ้างอิง 3",
                    a.refer_description3 AS "เกี่ยวข้องเป็น",
                    a.refer_telephone3 AS "เบอร์โทรอ้างอิง 3",
                    a.place_of_work AS "หน่วยงานที่ทำงาน",
                    a.office AS "บริษัทซัพคอนแทรค",
                    a.position AS "อาชีพ",
                    a.income_name AS "ประเภทเงินเดือน",
                    COALESCE(a.base_income, 0) AS "ฐานเงินเดือน",
                    a.income_amount AS "รายได้สุทธิ",
                    CASE 
                        WHEN a.status_approve = '1' THEN 'ผ่าน'
                        WHEN a.status_approve = '2' THEN 'ทำสัญญาแล้ว'
                        WHEN a.status_approve = '9' THEN 'ไม่ผ่าน'
                        WHEN a.status_approve = '5' THEN 'ยกเลิก' 
                        ELSE 'รออนุมัติ' 
                    END AS "สถานะอนุมัติ",
                    CASE 
                        WHEN a.car_type = 'N' THEN 'มือหนึ่ง'
                        WHEN a.car_type = 'U' THEN 'มือสอง' 
                    END AS "สถานะรถ",
                    a.apname AS "ร้านที่ออกรถ",
                    a.branch_name AS "สาขา",
                    a.model_name AS "รุ่น",
                    a.sales_person AS "เซลล์",
                    f.first_name AS "พนักงานเครดิต",
                    d.name AS "เกรด NCB",
                    a.condition_approve AS "หมายเหตุ"
                FROM View_InstallmentDetail a  
                LEFT JOIN auth_user b ON b.username = a.user_id
                LEFT JOIN Tb_MasterNCB d ON d.id = a.ncb_id
                LEFT JOIN auth_user f ON f.username = a.user_id
                WHERE a.created_at BETWEEN %s AND %s
                AND COALESCE(a.status_approve, 0) = %s     
                AND a.create_to_branch_id = %s 
                ORDER BY a.created_at
            """
            print("query: ", query % ("'%s'" % start_date, "'%s'" % end_date, status_approve, branch_id))
            cursor.execute(query, [start_date, end_date, status_approve, branch_id])

            columns_header = [col[0] for col in cursor.description]
            row_data = [
                dict(zip(columns_header, row))
                for row in cursor.fetchall()
            ]
        finally:
            cursor.close()

        rename_header = None
        return export_xlsx('รายงานการขออนุมัติสินเชื่อ.xlsx', row_data, rename_header)

def export_xlsx(filename, data, rename_column=None):
    df = pd.DataFrame.from_records(data)
    print('df : ',df)
    # เช็ค data type เพื่อ set format
    get_col_type = []
    if data:
        first_row = data[0]
        for key, value in first_row.items():
            index = list(first_row).index(key)
            get_col_type.append({
                'key': key,
                'type': type(value),
                'index': index,
            })
    # print(get_col_type)
    if get_col_type:
        for foo in get_col_type:
            if foo['type'] == Decimal:
                df[foo['key']] = pd.to_numeric(df[foo['key']])
    # print(df.dtypes)
    # เปลี่ยนชื่อ column
    if rename_column:
        df.rename(columns=rename_column, inplace=True)

    # Create xlsx file
    output = io.BytesIO()

    with pd.ExcelWriter(output, date_format='dd/mm/yyyy', datetime_format='dd/mm/yyyy HH:mm:ss') as writer:
        df.to_excel(writer, sheet_name="Sheet1", index=False)

        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

        # Create format
        currency_format = workbook.add_format({"num_format": "#,##0.00"})

        if get_col_type:
            for foo in get_col_type:
                if foo['type'] == Decimal:
                    # print(foo['key'], foo['index'])
                    worksheet.set_column(foo['index'], foo['index'], 20, currency_format)
        # print('ExcelWriter')
    # Set up the Http response.
    # response = HttpResponse(
    #     output.getvalue(),
    #     content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    # )
    response = JsonResponse({
        'content_type' : 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' ,
    })
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'%s' % quote(filename)
    # Response file
    print('response : ',response)
    print('response : ',response['Content-Disposition'])
    return response