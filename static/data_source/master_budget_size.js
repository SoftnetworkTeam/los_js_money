function dsMasterBudgetSize(url, pageSize = 10, data = {}) {
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
                    size_code: { type: "string" },
                    size_name: { type: "string" },
                    memo: { type: "string" },
                    status: { type: "string" },
                    status_name: { type: "string" }, // ต้องจัดการแปลง status เป็นชื่อใน backend
                    slug: { type: "string" },
                }
            }
        },
        sort: [
            {
                field: "size_code",
                dir: "asc"
            }
        ]
    });
}
