function dsMasterDocContGroup (url, pageSize=10, data={}){
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
                    cont_group: {type: "json"},
                    doc: {type: "json"},
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