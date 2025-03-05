function dsContractCustomer(url, pageSize = 10, data={}) {
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
                    cust_code: {type: "string"},
                    pre_name: {type: "json"},
                    first_name: {type: "string"},
                    last_name: {type: "string"},
                    cust_type: {type: "string"},
                    cust_type_name: {type: "string"},
                    customer_grade: {type: "json"},
                    card_no: {type: "string"},
                    telephone: {type: "string"},
                    mobile: {type: "string"},
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

