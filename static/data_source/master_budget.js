function dsMasterBudget(url, pageSize = 10, data = {}) {
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
                    budget_code: { type: "string" },
                    budget_name: { type: "string" },
                    status: { type: "string" },
                    status_name: { type: "string" }, // ต้องจัดการแปลง status เป็นชื่อใน backend
                    slug: { type: "string" },
                }
            }
        },
        sort: [
            {
                field: "budget_code",
                dir: "asc"
            }
        ]
    });
}
