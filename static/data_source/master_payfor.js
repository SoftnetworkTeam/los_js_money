function dsMasterPayfor (url, pageSize=10, data={}){
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
                    payfor_code: {type: "string"},
                    payfor_name: {type: "string"},
                    payfor_type: {type: "string"},
                    payfor_type_name: {type: "string"},
                    vat_status: {type: "string"},
                    vat_status_name: {type: "string"},
                    branch_paid: {type: "string"},
                    branch_paid_name: {type: "string"},
                    redeem_status: {type: "string"},
                    redeem_status_name: {type: "string"},
                    account_code: {type: "string"},
                    bill_payment_code: {type: "string"},
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

