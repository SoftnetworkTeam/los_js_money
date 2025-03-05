function dsMasterExpenseType(url, pageSize = 10, data = {}) {
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
                    expensetype_code: { type: "string" },
                    expensetype_name: { type: "string" },
                    expensetype_group: { type: "string" },
                    expensetype_group_name: { type: "string" },
                    branch_paid: { type: "string" },
                    branch_paid_name: { type: "string" },
                    gl_status: { type: "string" },
                    gl_status_name: { type: "string" },
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
                field: "expensetype_code",
                dir: "asc"
            }
        ]
    });
}
