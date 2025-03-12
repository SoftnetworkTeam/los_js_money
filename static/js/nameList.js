$(document).ready(function () {
    function statusFilter(element) {
        element.kendoDropDownList({
            dataTextField: "text",
            dataValueField: "value",
            dataSource: [
                {text: "ทั้งหมด", value: ""},
                {text: "Waiting", value: "0"},
                {text: "Approve", value: "1"},
                {text: "Cancel", value: "5"},
                {text: "Reject", value: "9"},
                {text: "Created Contract", value: "2"}
            ],
        });
    }

    $("#openDialogButton").kendoButton({
      cssClass: "custom-button"
    });

    var columns = [
            { title: "ลำดับ", template: "#= index #", width: "auto" },
            // { field: "apname", width: "auto", title: "ผู้จำหน่าย" },
            { field: "app_id", width: "auto", title: "เลขที่ขอสินเชื่อ" },
            {
                field: "created_at", title: "วันที่ขอสินเชื่อ",
                width: "auto",
                template: "#= kendo.toString(kendo.parseDate(created_at), 'dd/MM/yy') #",
                filterable: false
            },
            { field: "customer_name", width: "auto", title: "ชื่อ - นามสกุล" },
            { field: "card_no", width: "auto", title: "เลขที่บัตร" },
            {
                title: "สถานะสัญญา",
                width: "auto",
                field: "n_status_approve",
                template: function (dataItem) {
                    return dataItem.status_approve === 1 ? '<div class="badge badge-success badgeStatus">Approve</div>' :
                        dataItem.status_approve === 9 ? '<div class="badge badge-danger badgeStatus">Reject</div>' :
                            dataItem.status_approve === 2 ? '<div class="badge badge-info badgeStatus">Created Contract</div>' :
                                dataItem.status_approve === 5 ? '<div class="badge badge-danger badgeStatus">Cancel</div>' :
                                    '<div class="badge badge-warning badgeStatus">Waiting</div>';
                },
                filterable: {
                    ui: statusFilter,
                }
            },
            {
                title: "Action",
                width: "auto",
                template: function (dataItem) {
                    let detailUrl = 'name-list/detail/' + dataItem.id;
                    let editUrl = 'name-list/edit/' + dataItem.id;
      
                    let buttons = '<a href="' + detailUrl + '" ><button class="btn btn-outline-primary btn-sm" data-bs-toggle="tooltip" title="รายละเอียด"><i class="fa-solid fa-magnifying-glass"></i></button></a> ';
      
      
                    if (authEdit == 'True'){
                        if (dataItem.status_approve !== 2) {
                            buttons += '<a href="' + editUrl + '" ><button class="btn btn-outline-warning btn-sm" data-bs-toggle="tooltip" title="แก้ไขข้อมูล"><i class="fa-solid fa-pen-to-square"></i></button></a>';
                        }
                    }
                   
      
                    return buttons;
                },
                attributes: { style: "text-align: start;" },
            },
        ];

        let apiUrl = "/customer-api/all/";
        const path = window.location.pathname;

        if (path.includes("/name-list/approve")) {
            apiUrl = "/customer-api/approve/";
        } else if (path.includes("/name-list/waiting")) {
            apiUrl = "/customer-api/waiting/";
        }
      
        // เรียกใช้ฟังก์ชัน initKendoGrid
        initKendoGrid("#grid", apiUrl, columns, {
            apname: { type: "string" },
            app_id: { type: "string" },
            created_at: { type: "date" },
            customer_name: { type: "string" },
            card_no: { type: "string" }
        }, "app_id","desc");
});
