# file: myapp/context_processors.py

from userauth.models import UserAuth


def req_context(request):
    context = {}
    if request.user.id is not None:
        mid_user_auth = UserAuth.objects.filter(user=request.user)
        if mid_user_auth.exists():
            for foo in mid_user_auth:
                if foo.auth.auth_code == 'A001':
                    context["auth_reject_approve"] = foo.status
                elif foo.auth.auth_code == 'A002':
                    context["auth_edit_delete"] = foo.status
                elif foo.auth.auth_code == 'A003':
                    context["auth_insert_info"] = foo.status
                elif foo.auth.auth_code == 'A004':
                    context["auth_report_menu"] = foo.status
                elif foo.auth.auth_code == 'A005':
                    context["auth_permission_menu"] = foo.status
                elif foo.auth.auth_code == 'A006':
                    context["auth_branchap_menu"] = foo.status
                elif foo.auth.auth_code == 'A007':
                    context["auth_permission_user"] = foo.status
    return context
