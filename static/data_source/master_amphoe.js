function dsMasterAmphoe(url, pageSize = 10, data={}) {
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
                    province: {type: "json"},
                    amphoe_code: {type: "string"},
                    amphoe_name: {type: "string"},
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
                field: "province_id",
                dir: "asc"
            }, {
                field: "id",
                dir: "asc"
            }
        ]
    });
}

