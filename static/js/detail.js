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
                    success: function(response) {
                        Swal.fire('<p style="font-size : 18px">บันทึกสาเหตุการไม่อนุมัติสินเชื่อเรียบร้อยแล้ว<p>', '', 'success');
                        updateButtons(status,response.detail);
                    },
                    error: function(xhr) {
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
                    success: function(response) {
                        Swal.fire('<p style="font-size : 18px">บันทึกสาเหตุการยกเลิกสินเชื่อเรียบร้อยแล้ว<p>', '', 'success');  // Update message here
                        updateButtons(status,response.detail);
                    },
                    error: function(xhr) {
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
            success: function(response) {
                Swal.fire('<p style="font-size : 20px">อนุมัติเรียบร้อยแล้ว<p>', '', 'success');
                updateButtons(status,response.detail);
            },
            error: function(xhr) {
                Swal.fire('<p style="font-size : 20px">เกิดข้อผิดพลาด<p>', '', 'error');
            }
        });
    }
}

function updateButtons(status,detail) {
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

var templateDialog = `
  <div class="modal-body">
      <div class="d-block justify-content-center">
          <form
                  action="{% url 'print_report' %}"
                  autocomplete="off"
                  method="GET"
                  target="_blank"
          >
              <input
                      type="hidden"
                      id="reportnm"
                      name="report"
                      value="fr_customer_information.fr3"
              />
              <input type="hidden" name="format" value="PDF"/>
              <input type="hidden" name="s_app_id" id="s_app_id1" value="{{ customer_loan_detail.app_id }}"/>
              <div class="mb-2 text-center">
                  <button
                          type="submit"
                          id="submitBtn1"
                          class="btn btn-success w-100"
                  >
                      <i class="ti-printer mr-2"></i> แบบฟอร์มการตรวจสอบข้อมูลลูกค้า
                  </button>
              </div>
          </form>
      </div>
      <div class="d-block justify-content-center">
          <form
                  action="{% url 'print_report' %}"
                  autocomplete="off"
                  method="GET"
                  target="_blank"
          >
              <input
                      type="hidden"
                      id="reportnm"
                      name="report"
                      value="fr_credit_check.fr3"
              />
              <input type="hidden" name="format" value="PDF"/>
              <input type="hidden" name="s_app_id" id="s_app_id2" value="{{ customer_loan_detail.app_id }}"/>
              <div class="mb-2 text-center">
                  <button
                          type="submit"
                          id="submitBtn2"
                          class="btn btn-success w-100"
                  >
                      <i class="ti-printer mr-2"></i> ผลการตรวจสอบสินเชื่อเบื้องต้น
                  </button>
              </div>
          </form>
      </div>
      <div class="d-block justify-content-center">
          <form
                  action="{% url 'print_report' %}"
                  autocomplete="off"
                  method="GET"
                  target="_blank"
          >
              <input
                      type="hidden"
                      id="reportnm"
                      name="report"
                      value="fr_ncb_check.fr3"
              />
              <input type="hidden" name="format" value="PDF"/>
              <input type="hidden" name="s_app_id" id="s_app_id3" value="{{ customer_loan_detail.app_id }}"/>
              <div class="mb-2 text-center">
                  <button
                          type="submit"
                          id="submitBtn3"
                          class="btn btn-success w-100"
                  >
                      <i class="ti-printer mr-2"></i> ฟอร์มตรวจสอบข้อมูลเครดิตบูโร
                  </button>
              </div>
          </form>
      </div>
  </div>
`;




// function showModal() {
//   var modalContainer = document.getElementById('modal-container');

//   modalContainer.innerHTML = templateDialog;

// }

// // เรียกใช้ฟังก์ชันแสดง modal
// showModal();
