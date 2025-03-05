// check id card
function checkID(id) {
    if (id.length !== 13) return false;
    for (i = 0, sum = 0; i < 12; i++)
        sum += parseFloat(id.charAt(i)) * (13 - i);
    return (11 - sum % 11) % 10 === parseFloat(id.charAt(12));
}

// calculate age
function calculateAge(birthday) {
    return ~~((Date.now() - birthday) / (31557600000));
}

function isEmpty(obj) {
    for (var x in obj) {
        return false;
    }
    return true;
}

function isNumber(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
}

/**
 * check document running
 * @return {boolean}
 */
function DocRunning(document_id, branch_id) {
    var base_url = window.location.origin;
    let running = false;
    $.ajax({
        url: base_url+'/document_running/view_list',
        data: {
            'document': document_id,
            'branch': branch_id
        },
        async: false,
        //cache: false,
        success: function (response) {
            running = response.results[0].running;
        }
    });
    return running;
}

/**
 * generate slug
 * @return {string}
 */
function GenerateSlug() {
    let date = new Date();
    let formattedNumber = ("0" + date.getMilliseconds()).slice(-3);
    return date.getFullYear() + "" + (date.getMonth() + 1) + "" + date.getDate() + "" + date.getHours() + "" + date.getMinutes() + "" +
        date.getMinutes() + "" + date.getSeconds() + "" + formattedNumber;
}

//confirm
function ConfirmSave(callback) {
    bootbox.confirm({
        title: "ยืนยันการบันทึกข้อมูล",
        message: "<table>\n" +
            "    <tr>\n" +
            "        <td style=\"vertical-align: middle; width: 46px;\">\n" +
            "<i class=\"mdi mdi-help-circle mdi-36px\"></i></td>\n" +
            "        <td style=\"vertical-align: middle;\">ต้องการบันทึกข้อมูล?</td>\n" +
            "    </tr>\n" +
            "</table>",
        centerVertical: true,
        swapButtonOrder: true,
        buttons: {
            confirm: {
                label: 'OK',
                className: 'btn-info boot-box-fix-button'
            },
            cancel: {
                label: 'Cancel',
                className: 'btn-dark boot-box-fix-button pull-right  margin-left-10px'
            }
        },
        callback: function (result) {
            callback(result);
        }
    });
}

//Validator
function validExists(app_name, model_name, field_name, value, value_id=0) {
    var base_url = window.location.origin;
    let result = true;
    $.ajax({
        url: base_url + '/validate_exists',
        data: {
            'app_name': app_name,
            'model_name': model_name,
            'field_name': field_name,
            'value': value,
            'value_id': value_id,
        },
        async: false,
        success: function (response) {
            result = (response['is_valid'] === false);
        }
    });
    return result;
}

function validate_model_exists(app_name, model_name, field_name, value, brand, value_id=0) {
    var base_url = window.location.origin;
    let result = true;
    $.ajax({
        url: base_url + '/validate_exists',
        data: {
            'app_name': app_name,
            'model_name': model_name,
            'field_name': field_name,
            'value': value,
            'brand': brand,
            'value_id': value_id,
        },
        async: false,
        success: function (response) {
            result = (response['is_valid'] === false);
        }
    });
    return result;
}

function validate_sub_model_exists(app_name, model_name, field_name, value, model, value_id=0) {
    var base_url = window.location.origin;
    let result = true;
    $.ajax({
        url: base_url + '/validate_exists',
        data: {
            'app_name': app_name,
            'model_name': model_name,
            'field_name': field_name,
            'value': value,
            'model': model,
            'value_id': value_id,
        },
        async: false,
        success: function (response) {
            result = (response['is_valid'] === false);
        }
    });
    return result;
}
