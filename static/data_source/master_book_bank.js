function dsMasterBookBank(url, pageSize = 10, data={}) {
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
                    bank_id: {type: "integer"},
                    bank: {type: "json"},
                    bank_branch_id: {type: "integer"},
                    bank_branch: {type: "json"},
                    book_no: {type: "string"},
                    book_name: {type: "string"},
                    book_name_en: {type: "string"},
                    book_type: {type: "string"},
                    book_type_name: {type: "string"},
                    status: {type: "string"},
                    status_name: {type: "string"},
                    slug: {type: "string"},
                    created_at: {type: "date"},
                    updated_at: {type: "date"},
                }
            }
        },
        sort: [
            {
                field: "bank_id",
                dir: "asc"
            }, {
                field: "id",
                dir: "asc"
            }
        ]
    });
}

