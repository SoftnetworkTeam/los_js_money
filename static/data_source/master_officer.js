function dsMasterOfficer (url, pageSize=10, data={}){
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
                    officer_code: {type: "string"},
                    officer_name: {type: "string"},
                    department: {type: "json"},
                    status: {type: "string"},
                    status_name: {type: "string"},
                    billcoll_status: {type: "string"},
                    start_period: {type: "integer"},
                    end_period: {type: "integer"},
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

