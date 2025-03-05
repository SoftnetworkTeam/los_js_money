function dsMasterCartax (url, pageSize=10, data={}){
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
                    car_tax_code: {type: "string"},
                    car_tax_name: {type: "string"},
                    car_tax_desc: {type: "string"},
                    status: {type: "string"},
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

