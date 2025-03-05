let modal_search_name = '';
let modal_search_confirm_value = 0;
let modal_search_confirm_value2 = '';
let modal_search_confirm_elem = null;
let modal_search_param1 = '';

function OpenModalSearch(element, search_name, param1='') {
    let elem_modal_search = document.getElementById("modal_search");
    if (elem_modal_search) {
        $(elem_modal_search).modal();
        if (search_name !== modal_search_name) {
            $('#id_modal_search_value').val('');
        }
        modal_search_name = search_name;
        modal_search_confirm_elem = element;
        modal_search_param1 = param1;
        //
        GetPage(0);
    }
}

function GetPage(page) {
    let elem_search_result = document.getElementById("search_result");
    if (elem_search_result) {
        let search_result = $(elem_search_result);
        let search_value = $('#id_modal_search_value').val();
        let search_url = '';
        if (page === 0) {
            search_url = '/modal_search/' + modal_search_name
        } else {
            search_url = '/modal_search/' + modal_search_name + '?page=' + page
        }
        search_result.html('');
        modal_search_confirm_value = 0;
        $.ajax({
            async: false,
            cache: false,
            url: search_url,
            type: 'GET',
            data: {
                'search_value': search_value,
                'param1': modal_search_param1,
            },
            success: function (data) {
                search_result.html(data);
                $('#id_modal_search_confirm').attr('disabled', true);
            }
        });
    }
}

function SelectRow(row) {
    let elem_search_result = document.getElementById("search_result");
    $(elem_search_result).find('.modal_search_row').removeClass('selected');
    $(".modal_search_row_" + row).addClass("selected");
    //console.log($(".modal_search_row_" + row));
    $('#id_modal_search_confirm').attr('disabled', false);
    modal_search_confirm_value = row;
    //
    modal_search_confirm_value2 = $(".modal_search_row_" + row).find('.modal_search_field').html();
}

$(document).ready(function () {
    $('#id_search_button').on("click", function (e) {
        e.preventDefault();
        GetPage(0);
    });
    $('#id_modal_search_confirm').on("click", function (e) {
        e.preventDefault();
        if ((modal_search_confirm_elem)||(modal_search_confirm_elem !== '')) {
            let search_confirm_elem_temp = $('#'+modal_search_confirm_elem).attr('id') + '_temp';
            let modal_search_confirm_elem_temp = document.getElementById(search_confirm_elem_temp);
            //console.log(modal_search_confirm_elem_temp);
            $('#'+modal_search_confirm_elem).val(modal_search_confirm_value);
            if (modal_search_confirm_elem_temp) {
                $(modal_search_confirm_elem_temp).val(modal_search_confirm_value2.trim());
                $(modal_search_confirm_elem_temp).trigger('change');
                $(modal_search_confirm_elem_temp).trigger('focus');
            }
        }
    });
    $('#id_modal_search_value').on("keypress", function (e) {
        if (e.which === 13) {
            GetPage(0);
        }
    });
});