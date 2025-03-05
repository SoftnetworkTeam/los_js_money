function dsMasterContGroup (url, pageSize=10, data={}){
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
                    cont_type: {type: "string"},
                    cont_type_name: {type: "string"},
                    group_code: {type: "string"},
                    group_name: {type: "string"},
                    payment_terms: {type: "string"},
                    payment_terms_name: {type: "string"},
                    sequence_method: {type: "string"},
                    sequence_method_name: {type: "string"},
                    penalty_late: {type: "integer"},
                    pn_status: {type: "string"},
                    pn_status_name: {type: "string"},
                    writeoff_status: {type: "string"},
                    writeoff_status_name: {type: "string"},
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
                field: "id",
                dir: "asc"
            }
        ]
    });
}

