function dsMasterDocContractGroup (url, pageSize=10, data={}){
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
                    group_code: {type: "string"},
                    group_name: {type: "string"},
                    cont_group: {type: "integer"},
                    doc: {type: "integer"},
                    status_name: {type: "string"},
                    slug: {type: "string"},
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