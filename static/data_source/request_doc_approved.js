function dsRequestDocApproved(url, pageSize=10, data={}){
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
                    request_no: {type: "string"},
                    request_date: {type: "string"},
                    withdraw: {type: "string"},
                    send: {type: "string"},
                    deliver: {type: "string"},
                    contract: {type: "string"},
                    contract_detail: {type: "string"},
                    bill_status: {type: "string"},
                    internal_book: {type: "string"},
                    status: {type: "string"},
                    status_name: {type: "string"},
                    approve_status: {type: "string"},
                    slug: {type: "string"},
                    created_at: {type: "date"},
                    updated_at: {type: "date"},
                }
            }
        },
        sort: [
            {
                field: "id",
                dir: "desc"
            }
        ]
    });
}

