$(document).ready(function () {
    datepickerRange("#rangDate");
});

function exports(type) {
    var startDate = $('#startDateInput').val();
    var endDate = $('#endDateInput').val();
    var status = $('#status').val();

    var formData = new FormData();
    formData.append('start_date', startDate);
    formData.append('end_date', endDate);
    formData.append('status_approve', status);

    if (type === 'requestLoan') {
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/report/', true);
        xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
        xhr.responseType = 'blob'; 

        xhr.onload = function () {
            if (xhr.status === 200) {
                var blob = new Blob([xhr.response], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
                var link = document.createElement('a');
                link.href = window.URL.createObjectURL(blob);
                link.download = 'รายงานการขออนุมัติสินเชื่อ.xlsx';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            } else {
                console.error('Export error:', xhr.statusText);
            }
        };
        
        xhr.send(formData);
    }
}

