from django.urls import path
import base64
from django.conf import settings
from urllib.parse import parse_qs, urlencode
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from requests.structures import CaseInsensitiveDict
import requests
from theme.models import MasterBrand,MasterOfficer

def report(request, type):
    return render(request, "report.html")

def print_report(request):
    report_server_string = settings.FR_SERVER
    query_dict = parse_qs(request.META['QUERY_STRING'])
    new_query_dict = {}
    for foo in query_dict:
        if foo == 's_status_approve':
            master_s_status_approve = query_dict.get("s_status_approve", [None])[0]
            if master_s_status_approve != 'A':
                master_s_status_approve = master_s_status_approve + '%'
                master_s_status_approve = master_s_status_approve.encode('ascii')
            else:
                master_s_status_approve = '%'.encode('ascii')
            master_s_status_approve = base64.b64encode(master_s_status_approve).decode("utf-8", "ignore")
            new_query_dict['s_status_approve'] = master_s_status_approve
        else:
            new_query_dict[foo] = query_dict.get(foo, [None])[0]

    new_query_string = urlencode(new_query_dict)
    fr_headers = CaseInsensitiveDict()
    fr_headers["Accept"] = "application/pdf"
    fr_url = "{}://{}:{}/result?{}".format(report_server_string['PROTOCOL'], report_server_string['HOST'],
            report_server_string['PORT'],
            new_query_string)
    try:
        resp = requests.get(fr_url, headers=fr_headers)
    except Exception as e:
        return HttpResponseNotFound(e)
    else:
        content_disposition = resp.headers.get('Content-Disposition', 'inline; filename="report.pdf"')
        
        # ตั้งค่าให้เป็น "attachment" สำหรับดาวน์โหลด
        # content_disposition = 'attachment; filename="report.pdf"'
        
        resp_headers = resp.headers
        response = HttpResponse(resp.content, content_type='application/pdf',)
        response['Server'] = 'LMS Report Server'
        response['Content-Disposition'] = content_disposition
        response['Cache-Control'] = resp_headers['Cache-Control']
        response['Pragma'] = resp_headers['Pragma']
        response['Accept-ranges'] = resp_headers['Accept-ranges']
        response['Last-Modified'] = resp_headers['Last-Modified']
        response['Expires'] = resp_headers['Expires']
        response['X-Powered-By'] = resp_headers['X-Powered-By']
        response['FastReport-container'] = resp_headers['FastReport-container']
        return response

