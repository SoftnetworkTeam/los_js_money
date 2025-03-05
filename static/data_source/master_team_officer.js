function dsMasterDocReviewTeamOfficer(url, pageSize = 10, data={}) {
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
                    team_info: {type: "json"},
                    officer: {type: "json"},
                    worked_no: {type: "integer"},
                    slug: {type: "string"},
                    created_at: {type: "date"},
                    updated_at: {type: "date"},
                }
            }
        },
        sort: [
            {
                field: "team_info_id",
                dir: "asc"
            }, {
                field: "id",
                dir: "asc"
            }
        ]
    });
}

