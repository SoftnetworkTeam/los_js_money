function dsMasterStrongLocker(url, pageSize = 10, data = {}) {
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
                    locker_code: {type: "string"},
                    locker_name: {type: "string"},
                    strong: {type: "json"},
                    status: {type: "string"},
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