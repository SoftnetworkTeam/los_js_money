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

def report(request, type):
    return render(request, "report.html")


class reports(View):
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
                    COALESCE(a.base_income, 0) AS "ฐานเงินเดือน",
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
                WHERE a.created_at BETWEEN %s AND %s
                AND a.create_to_branch_id = %s 
                AND a.company_id = %s
            """

            params = [start_date, end_date, branch_id,company_id]

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

