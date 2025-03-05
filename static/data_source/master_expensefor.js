function dsMasterExpenseFor(url, pageSize = 10, data = {}) {
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
                    id: { type: "integer" },
                    expensefor_code: { type: "string" },
                    expensefor_name: { type: "string" },
                    direct_cost: { type: "string" },
                    direct_cost_name: { type: "string" },
                    branch_paid: { type: "string" },
                    branch_paid_name: { type: "string" },
                    status: { type: "string" },
                    status_name: { type: "string" },
                    slug: { type: "string" },
                    created_at: { type: "date" },
                    updated_at: { type: "date" },
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
