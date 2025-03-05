function dsMasterPaytype (url, pageSize=10, data={}){
    return new kendo.data.DataSource({
        pageSize: pageSize,
        serverPaging: true,
        serverFiltering: true,
        serverSorting: true,
        transport: {
            read: {
                url: url,
                dataType: "json",
                type: "GET",
                data: data,
            }
        },
        schema: {
            data: "results",
            total: "count",
            model: {
                fields: {
                    id: {type: "integer"},
                    paytype_code: {type: "string"},
                    paytype_name: {type: "string"},
                    paytype_group: {type: "string"},
                    paytype_group_name: {type: "string"},
                    branch_paid: {type: "string"},
                    branch_paid_name: {type: "string"},
                    gl_status: {type: "string"},
                    gl_status_name: {type: "string"},
                    account_code: {type: "string"},
                    bill_payment_bank: {type: "string"},
                    status: {type: "string"},
                    status_name: {type: "string"},
                    slug: {type: "string"},
                    created_at: {type: "date"},
                    updated_at: {type: "date"},
                }
            }
        },
        sort: [
            {
                field: "id",
                dir: "asc"
            }
        ]
    });
}

