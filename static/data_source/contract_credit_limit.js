function dsContractCreditLimit(url, pageSize = 10, data={}) {
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
                    branch: {type: "json"},
                    customer: {type: "json"},
                    credit_no: {type: "string"},
                    credit_date: {type: "date"},
                    credit_sequence: {type: "number"},
                    credit_limit: {type: "number"},
                    credit_using: {type: "number"},
                    credit_hold: {type: "number"},
                    credit_balance: {type: "number"},
                    credit_apply_date: {type: "date"},
                    credit_status: {type: "string"},
                    credit_status_name: {type: "string"},
                    approve_status: {type: "string"},
                    approve_status_name: {type: "string"},
                    approve_date: {type: "date"},
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

