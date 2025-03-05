function dsMasterCarUsageDetailType(url, pageSize = 10, data = {}) {
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
            data: "results", // ระบุชื่อ field ที่ใช้เก็บรายการข้อมูล
            total: "count",  // ระบุชื่อ field ที่ใช้เก็บจำนวนข้อมูลทั้งหมด
            model: {
                fields: {
                    id: { type: "integer" },
                    car_detail_code: { type: "string" },
                    car_detail_name: { type: "string" },
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
                field: "car_detail_code",
                dir: "asc"
            }
        ]
    });
}
