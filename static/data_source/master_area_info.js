function dsMasterAreaInfo(url, pageSize = 10, data = {}) {
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
                    area_code: { type: "string" },
                    area_name: { type: "string" },
                    status: { type: "string" },
                    slug: { type: "string" },
                    created_at: { type: "date" },
                    updated_at: { type: "date" },
                }
            }
        },
        sort: [
            {
                field: "id",
                dir: "asc" // เรียงตาม id
            }
        ]
    });
}
