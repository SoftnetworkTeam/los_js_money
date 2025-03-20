$(document).ready(function () {
    loadSelect2Data(urlMasterscoringinfo, ".js-data-scoringinfo-ajax", "results", "id", "score_name");
    var form_data = {
        "score_set": score_set,
        "customer_age": customer_age,
        "occupation": occupation,
        "education": education,
        "minorchildren": minorchildren,
        "business_age": business_age,
        "reason": reason,
        "residence": residence,
        "living_type": living_type,
        "business_type": business_type,
        "profit": profit,
        "category_occupation": category_occupation,
        "shop_type": shop_type,
        "rentalage": rentalage
    };

    $.ajax({
        url: urlCalScoring,
        data: form_data,
        type: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        success: function (response) {
            if (response.status === 'success') {
                $('#score_1').text(response.score_1);
                $('#score_2').text(response.score_2);
                $('#score_3').text(response.score_3);
                $('#grade').text(response.grade);

                if (response.message == 'แนะนำให้อนุมัติ') {
                    $('#guide').html(`<br>
                            <div style="background-color: #03A9F3; color: white; padding: 10px; text-align: center; font-weight: bold;">
                                คำแนะนำระบบ : ผู้ขอกู้มีคะแนนที่ดีและหนี้ต่อได้รายได้ผ่านเกณฑ์ แนะนำให้อนุมัติ
                            </div>
                        `);
                    $('.approve').removeClass('d-none')
                } else {
                    $('#guide').html(`
                        <div style="background-color:rgb(218, 57, 70); color: white; padding: 10px; text-align: center; font-weight: bold;">
                            คำแนะนำระบบ : ผู้ขอกู้มีคะแนนที่ไม่ดีและหนี้ต่อได้รายได้ไม่ผ่านเกณฑ์ แนะนำ ไม่ให้อนุมัติ
                        </div>
                    `);
                    $('.approve').addClass('d-none')
                }
            }
        }
    });

    // กดที่ .js-data-scoringinfo-ajax ส่ง AJAX
    $(document).on("change", ".js-data-scoringinfo-ajax", function () {

        var form_data = {
            "score_set": $('.js-data-scoringinfo-ajax').val(),
            "customer_age": customer_age,
            "occupation": occupation,
            "education": education,
            "minorchildren": minorchildren,
            "business_age": business_age,
            "reason": reason,
            "residence": residence,
            "living_type": living_type,
            "business_type": business_type,
            "profit": profit,
            "category_occupation": category_occupation,
            "shop_type": shop_type,
            "rentalage": rentalage
        };

        $.ajax({
            url: urlCalScoring,
            data: form_data,
            type: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            success: function (response) {
                if (response.status === 'success') {
                    $('#score_1').text(response.score_1);
                    $('#score_2').text(response.score_2);
                    $('#score_3').text(response.score_3);
                    $('#grade').text(response.grade);

                    if (response.message === 'แนะนำให้อนุมัติ') {
                        $('#guide').html(`
                                <div style="background-color: #03A9F3; color: white; padding: 10px; text-align: center; font-weight: bold;">
                                    คำแนะนำระบบ : ผู้ขอกู้มีคะแนนที่ดีและหนี้ต่อได้รายได้ผ่านเกณฑ์ แนะนำให้อนุมัติ
                                </div>
                            `);
                        $('.approve').removeClass('d-none')
                    } else {
                        $('#guide').html(`
                            <div style="background-color:rgb(218, 57, 70); color: white; padding: 10px; text-align: center; font-weight: bold;">
                                คำแนะนำระบบ : ผู้ขอกู้มีคะแนนที่ดีและหนี้ต่อได้รายได้ไม่ผ่านเกณฑ์ แนะนำ ไม่ให้อนุมัติ
                            </div>
                        `);
                        $('.approve').addClass('d-none')
                    }
                }
            }
        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.querySelectorAll(".fileLink").forEach(link => {
    link.addEventListener("click", function (event) {
        event.preventDefault(); // ป้องกันการเปิดลิงก์ทันที
        let fileLink = this.getAttribute("href");

        fetch(fileLink, { method: 'HEAD' })
            .then(response => {
                if (response.ok) {
                    window.open(fileLink, '_blank');
                } else {
                    window.open('https://www.google.com', '_blank');
                }
            })
            .catch(error => {
                console.error('Error checking file link:', error);
                window.open('https://www.google.com', '_blank');
            });
    });
});


function notification(d_title, d_text, d_icon, d_btn_text) {
    $(document).ready(function () {
        Swal.fire({
            title: d_title,
            text: d_text,
            icon: d_icon,
            confirmButtonText: d_btn_text,
            allowOutsideClick: false
        })
    });
}

function approve(status) {
    var csrf_token = getCookie('csrftoken');
    if (status == 9) {
        Swal.fire({
            title: '<span style="font-size: 18px;">สาเหตุการไม่อนุมัติสินเชื่อ</span>',
            html: '<textarea id="swal-textarea" maxlength="1024" placeholder="กรุณากรอกข้อความไม่เกิน 1024 ตัวอักษร" style="width: 100%; height: 100px; font-size: 16px; resize: none; border: 1px solid #ccc; border-radius: 8px; padding: 8px; outline: none; transition: border-color 0.3s;"></textarea>',
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: 'ตกลง',
            cancelButtonText: 'ยกเลิก',
            preConfirm: () => {
                const textarea = document.getElementById('swal-textarea');
                const value = textarea.value.trim();

                if (!value) {
                    Swal.showValidationMessage('กรุณากรอกข้อความก่อนยืนยัน');
                    return false;
                }
                if (value.length > 1024) {
                    Swal.showValidationMessage('กรุณากรอกข้อความไม่เกิน 1024 ตัว');
                    return false;
                }
                return value;
            }
        }).then((result) => {
            if (result.isConfirmed) {
                const issue_cancel = result.value;
                $.ajax({
                    url: "",
                    type: "POST",
                    headers: {
                        'X-CSRFToken': csrf_token
                    },
                    data: {
                        installment_id: $("#installment_id").val(),
                        status: status,
                        issue_cancel: issue_cancel,
                        csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
                    },
                    success: function (response) {
                        Swal.fire('<p style="font-size : 18px">บันทึกสาเหตุการไม่อนุมัติสินเชื่อเรียบร้อยแล้ว<p>', '', 'success');
                        updateButtons(status, response.detail);
                    },
                    error: function (xhr) {
                        Swal.fire('<p style="font-size : 18px">เกิดข้อผิดพลาด<p>', '', 'error');
                    }
                });
            }
        });

        const styleTag = document.createElement('style');
        styleTag.innerHTML =
            '#swal-textarea:focus {border-color: #2196F3; box-shadow: 0 0 8px rgba(33, 150, 243, 0.5);}';
        document.head.appendChild(styleTag);
    } else if (status == 5) {
        Swal.fire({
            title: '<span style="font-size: 18px;">สาเหตุการยกเลิกเอกสารคำขอสินเชื่อ</span>',
            html: '<textarea id="swal-textarea" maxlength="1024" placeholder="กรุณากรอกไม่เกิน 1024 ตัวอักษร" style="width: 100%; height: 100px; font-size: 16px; resize: none; border: 1px solid #ccc; border-radius: 8px; padding: 8px; outline: none; transition: border-color 0.3s;"></textarea>',
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: 'ตกลง',
            cancelButtonText: 'ยกเลิก',
            preConfirm: () => {
                const textarea = document.getElementById('swal-textarea');
                const value = textarea.value.trim();

                if (!value) {
                    Swal.showValidationMessage('กรุณากรอกข้อความก่อนยืนยัน');
                    return false;
                }
                if (value.length > 1024) {
                    Swal.showValidationMessage('กรุณากรอกข้อความไม่เกิน 1024 ตัว');
                    return false;
                }
                return value;
            }
        }).then((result) => {
            if (result.isConfirmed) {
                const issue_cancel = result.value;

                $.ajax({
                    url: "",
                    type: "POST",
                    headers: {
                        'X-CSRFToken': csrf_token
                    },
                    data: {
                        installment_id: $("#installment_id").val(),
                        status: status,
                        issue_cancel: issue_cancel,
                        csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
                    },
                    success: function (response) {
                        Swal.fire('<p style="font-size : 18px">บันทึกสาเหตุการยกเลิกสินเชื่อเรียบร้อยแล้ว<p>', '', 'success');
                        updateButtons(status, response.detail);
                    },
                    error: function (xhr) {
                        Swal.fire('<p style="font-size : 18px">เกิดข้อผิดพลาด<p>', '', 'error');
                    }
                });
            }
        });

        const styleTag = document.createElement('style');
        styleTag.innerHTML =
            '#swal-textarea:focus {border-color: #2196F3; box-shadow: 0 0 8px rgba(33, 150, 243, 0.5);}';
        document.head.appendChild(styleTag);
    } else {
        $.ajax({
            url: "",
            type: "POST",
            headers: {
                'X-CSRFToken': csrf_token
            },
            data: {
                installment_id: $("#installment_id").val(),
                status: status,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
            },
            success: function (response) {
                Swal.fire('<p style="font-size : 20px">อนุมัติเรียบร้อยแล้ว<p>', '', 'success');
                updateButtons(status, response.detail);
            },
            error: function (xhr) {
                Swal.fire('<p style="font-size : 20px">เกิดข้อผิดพลาด<p>', '', 'error');
            }
        });
    }
}

function updateButtons(status, detail) {
    $(".col.justify-content-start.my-3").empty();
    $(".col.justify-content-start.my-3").append('<a href="/name-list"><button type="button" class="btn btn-outline-primary mx-2">ย้อนกลับ</button></a>');
    $("#notAppoveIssue, #cancelIssue,#statusApprove,#detailIssue").hide();

    if (status == 1) {
        $(".col.justify-content-start.my-3").append('<button type="button" class="btn btn-outline-danger mx-2" onclick="approve(9)">ไม่อนุมัติ</button>');
        $("#statusApproveNew").html('<span class="badge badge-success ms-2 badgeStatus">Approve</span>');
        $("#detailCancelIssueNew,#detailNotAppoveIssueNew,#notAppoveIssue,#cancelIssue,#notAppoveIssueNew,#cancelIssueNew").hide();
    } else if (status == 9) {
        $(".col.justify-content-start.my-3").append('<button type="button" class="btn btn-outline-success" onclick="approve(1)">อนุมัติ</button>');
        $("#statusApproveNew").html('<span class="badge badge-danger ms-2 badgeStatus">Reject</span>');
        $("#notAppoveIssueNew").html('<div>สาเหตุการไม่อนุมัติสินเชื่อ</div>').show();
        $("#detailNotAppoveIssueNew").html('<b class="text-red text-wrap">' + detail + '</b>').show();
        $("#detailCancelIssueNew").hide();
    } else if (status == 5) {
        $(".col.justify-content-end.my-3").empty();
        $("#statusApproveNew").html('<span class="badge badge-danger ms-2 badgeStatus">Cancel</span>');
        $("#cancelIssueNew").html('<div>สาเหตุการยกเลิกเอกสารคำขอสินเชื่อ</div>').show();
        $("#detailCancelIssueNew").html('<b class="text-red text-wrap">' + detail + '</b>').show();
        $("#detailAppoveIssueNew").hide();
    }
}


function confirmDelete(fileId) {
    notification_v2(
        'แจ้งเตือน',
        'กดตกลงเพื่อยืนยันการลบไฟล์',
        'warning',
        'ตกลง',
        'ยกเลิก',
        function () {
            $.ajax({
                url: "/detaildelete/" + fileId + "/",
                type: "GET",
                success: function (response) {
                    console.log(response);
                    Swal.fire({
                        title: "Deleted!",
                        icon: "success"
                    }).then(() => {
                        $('#confirmDelete-' + fileId).remove();
                    });
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.error(jqXHR.responseText);
                    Swal.fire({
                        title: "Error!",
                        text: "An error occurred while deleting the file.",
                        icon: "error"
                    });
                }
            });
        }
    );
}

