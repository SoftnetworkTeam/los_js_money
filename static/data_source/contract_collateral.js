function dsContractCollateral(url, pageSize = 10, data={}) {
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
                    collateral_type: {type: "string"},
                    collateral_type_name: {type: "string"},
                    product_type: {type: "json"},
                    chassis_no: {type: "string"},
                    engine_no: {type: "string"},
                    price_estimate: {type: "number"},
                    reg_no: {type: "string"},
                    province: {type: "json"},
                    status: {type: "string"},
                    status_name: {type: "string"},
                    slug: {type: "string"},
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

