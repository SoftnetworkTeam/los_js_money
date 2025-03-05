from userauth.models import UserAuth


class AuthUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        if response.context_data and request.user.id is not None:
            mid_user_auth = UserAuth.objects.filter(user=request.user)
            if mid_user_auth.exists():  # แก้ไขที่นี่
                for foo in mid_user_auth:
                    # สิทธิการอนุมัติและไม่อนุมัติ
                    if foo.auth.auth_code == 'A001':
                        response.context_data["auth_reject_approve"] = foo.status
                    # สิทธิการแก้ไขและลบ
                    elif foo.auth.auth_code == 'A002':
                        response.context_data["auth_edit_delete"] = foo.status
                    # สิทธิการเพิ่มข้อมูล
                    elif foo.auth.auth_code == 'A003':
                        response.context_data["auth_insert_info"] = foo.status
                    # สิทธิการเข้าถึงเมนูรายงาน
                    elif foo.auth.auth_code == 'A004':
                        response.context_data["auth_report_menu"] = foo.status
        return response
