function dsMasterSendByWithDraw (url, pageSize=10, data={}){
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
                    send_code: {type: "string"},
                    send_name: {type: "string"},
                    send_type: {type: "string"},
                    status: {type: "string"},
                    withdraw_document_name: {type: "string"},
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

