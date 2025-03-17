$(document).ready(function () {
    datepickerRange("#rangDate");

    function datepickerRange(inputSelector) {
        const currentDate = new Date();
        const startDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), 1);
        const endDate = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 0);  // +1 คือเดือนถัดไป 0 คือวันที่สุดท้ายของเดือนก่อนหน้า
        const startFormatted = formatDate(startDate);
        const endFormatted = formatDate(endDate);

        $(inputSelector).flatpickr({
            mode: "range",
            dateFormat: "d/m/Y",
            altInput: true,
            altFormat: "d/m/Y",
            allowInput: false,
            defaultDate: [startFormatted, endFormatted],
            locale: {
                weekdays: {
                    shorthand: ["อา.", "จ.", "อ.", "พ.", "พฤ.", "ศ.", "ส."],
                    longhand: ["อาทิตย์", "จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์"]
                },
                months: {
                    shorthand: ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."],
                    longhand: ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"]
                }
            },
            onChange: function (selectedDates, dateStr, instance) {
                if (selectedDates.length === 2) {
                    // แทนที่คำว่า "to" ด้วย "ถึง"
                    let formattedDate = dateStr.replace(" to ", " ถึง ");
                    $(inputSelector).val(formattedDate);
                    $(instance.altInput).val(formattedDate);
                }
                const startDate = formatDate(selectedDates[0]);
                const endDate = formatDate(selectedDates[1]);

                $('#startDateInput').val(startDate);
                $('#endDateInput').val(endDate);
            },
            onReady: function (selectedDates, dateStr, instance) {
                if (dateStr.indexOf(" to ") !== -1) {
                    let formattedDate = dateStr.replace(" to ", " ถึง ");
                    $(inputSelector).val(formattedDate);
                    $(instance.altInput).val(formattedDate);
                }
                const currentDate = new Date();
                const startDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), 1);
                const endDate = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 0);

                const startFormatted = formatDate(startDate);
                const endFormatted = formatDate(endDate);

                $('#startDateInput').val(startFormatted);
                $('#endDateInput').val(endFormatted);
            }
        });
    }
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
        $.ajax({
            url: '/exports/',
            type: 'POST',
            dataType: 'json',
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
            data: formData,
            processData: false, 
            contentType: false,  
            success: function (response) {
                var blob = new Blob([response], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
                var link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = 'รายงานการขออนุมัติสินเชื่อ.xlsx'; 
                link.click(); 
            },
            error: function (xhr, status, error,response) {
                console.error('Export error57755:');
               
            }
        });
    }
}

