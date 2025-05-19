$(document).ready(function () {
    datepickerRange("#rangDate");
});

async function exports(type) {
    var startDate = $('#startDateInput').val();
    var endDate = $('#endDateInput').val();
    var status = $('#status').val();
    var branch_id = $('#branch_id_report').val();


    var formData = new FormData();
    formData.append('start_date', startDate);
    formData.append('end_date', endDate);
    formData.append('status_approve', status);
    formData.append('branch_id', branch_id);


    if (type === 'requestLoan') {
        try {
            let response = await fetch('/exports/', {
                method: 'POST',
                body: formData,
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                },
            });

            let blob = await response.blob();
            let link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.download = 'รายงานการขออนุมัติสินเชื่อ.xlsx';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        } catch (error) {
            console.error('Export error:', error);
        }
    }
}