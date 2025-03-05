$(document).ready(function () {

    $("#openDialogButton").kendoButton({
      cssClass: "custom-button"
    });

    
    var url_userauth = window.location.href.includes("userauth");
    var url_editauth = window.location.href.includes("edit");

    
    var pathParts = window.location.pathname.split("/");
    var id = pathParts[pathParts.length - 1] || pathParts[pathParts.length - 2];

    console.log('url_url_userauth555',url_userauth)

    console.log('url_editauth555',url_editauth)
    console.log('id',id)

    var title_1 = "";
    var title_2 = "";
    var title_3 = "";
    var title_4 = "";
    var field_1 = "";
    var field_2 = "";
    var field_3 = "";
    var field_4 = "";

    if (url_userauth && !url_editauth) {
        title_1 = "<b>ลำดับ</b>";
        title_2 = "<b>ชื่อ - นามสกุล</b>";
        title_3 = "username";
        title_4 = "อีเมล์";
        field_2 = "first_name";
        field_3 = "username";
        field_4 = "email";
    } else if (url_userauth && url_editauth) {
        title_1 = "<b>ลำดับ</b>";
        title_2 = "<b>รหัสสิทธิ์การใช้งาน</b>";
        title_3 = "<b>ชื่อสิทธิ์การใช้งาน</b>";
        field_2 = "auth.auth_code";
        field_3 = "auth.auth_name";
    }

    var columns = [
        { 
            title: title_1, 
            width: 10,
            template: function (dataItem) {
                return dataItem.index || "";
            }
        },
        { field: field_2, width: 10, title: title_2 },
        { field: field_3, width: 50, title: title_3 },
    ];

    if (url_userauth && !url_editauth) {
        columns.push(
            { field: field_4, width: "auto", title: title_4 },
            {
                title: "<b>Action</b>",
                width: 117,
                template: function (dataItem) {
                    let editUrl = '/userauth/edit/' + dataItem.id;
                    let buttons = '';

                    if (typeof authEdit !== 'undefined' && authEdit) {
                        if (dataItem.status_approve !== 2) {
                            buttons += `<a href="${editUrl}">
                                <button class="btn btn-warning btn-sm" data-bs-toggle="tooltip" title="แก้ไขข้อมูล">
                                    <i class="fa-solid fa-pen-to-square"></i>
                                </button>
                            </a>`;
                        }
                    }
                    return buttons;
                },
                attributes: { style: "text-align: start;" },
            }
        );
    } else if (url_editauth && url_userauth) {
        columns.push({
            title: "<b>สถานะ</b>",
            width: 117,
            field: "auth.status",
            template: function (dataItem) {
                return `
                <div class="d-flex justify-content-between border-0" id="status-${dataItem.id}">
                    <ul class="nav nav-tabs dzm-tabs" role="tablist" style="background-color: #ebebeb;">
                        <li class="nav-item" role="presentation" onclick="changStatus('active', '${dataItem.id}','userauth','t','statusUserauth','${id}')">
                            <button class="nav-link btn btn-success btn-sm" type="button" role="tab" aria-selected="false"${dataItem.status === true ? ' style="background-color: #3AC977;" ' : ""} id="status-active-${dataItem.id}">
                                ใช้งาน
                            </button>
                        </li>
                        <li class="nav-item" role="presentation" onclick="changStatus('inActive', '${dataItem.id}','userauth','f','statusUserauth','${id}')">
                            <button class="nav-link btn btn-danger btn-sm" type="button" role="tab" aria-selected="true" ${dataItem.status === false ? ' style="background-color: #FF5E5E;" ' : ""} id="status-inactive-${dataItem.id}">ไม่ใช้งาน
                            </button>
                        </li>
                    </ul>
                </div>`;
            },
        });
    }


    if (url_userauth && !url_editauth) {
        initKendoGrid("#grid", "/userauth-api/", columns, {
            id: { type: "number" },
            first_name: { type: "string" },
            username: { type: "string" },
            email: { type: "string" }
        }, "id",'asc');
    } else if (url_editauth && url_userauth) {
        initKendoGrid("#gridEdit", "/edit-auth-api/"+id+"/", columns, {
            auth_code: { type: "string" },
            auth_name: { type: "string" },
            status: {type: "boolean"},
            id: {type: "number"}
        }, "auth_code",'asc');
    }
});

