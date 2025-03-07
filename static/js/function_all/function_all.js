$(document).ready(function () {
  const searchInput = $("#menuSearch");
  const menuItems = $("#menu > li");
  const noMenuMessage = $("#noMenuMessage");
  $('.select2').select2();

  searchInput.on("input", function () {
    const filter = searchInput.val().toLowerCase();
    let hasVisibleMenu = false;

    menuItems.each(function () {
      const item = $(this);
      const text = item.text().toLowerCase();

      if (item.hasClass("menu-title")) {
        item.show(); 
      } else if (text.includes(filter)) {
        item.show();
        hasVisibleMenu = true;
      } else {
        item.hide(); 
      }
    });

    if (filter && !hasVisibleMenu) {
      noMenuMessage.show();
    } else {
      noMenuMessage.hide();
    }
  });

  const initials = $("#firstName").text().charAt(0);
  $("#profileImage-1").text(initials);
  $("#profileImage-2").text(initials);

  if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
  }

  $(".js-data-nameList-ajax").select2({
    width: "100%",
    ajax: {
      url: "MasterBranchAP/",
      dataType: "json",
      delay: 250,
      data: function (params) {
        return {
          q: params.term,
          page: params.page,
        };
      },
      processResults: function (data, params) {
        params.page = params.page || 1;

        return {
          results: data.items,
          pagination: {
            more: params.page * 30 < data.total_count,
          },
        };
      },
      cache: true,
    },
    placeholder: "ค้นหา",
    escapeMarkup: function (markup) {
      return markup;
    },
    minimumInputLength: 0,
    templateResult: formatRepo,
    templateSelection: formatRepoSelection,
  });

  kendo.culture("th-TH");  // ตั้งค่าภาษาไทย

});

// document.querySelectorAll('#example [data-bs-toggle="tooltip"]')
//   .forEach(function (tooltipTriggerEl) {
//     new bootstrap.Tooltip(tooltipTriggerEl, {
//       container: "#example",
//     });
//   });

function showToast(icon, title, msg, position) {
  $(document).ready(function () {
    toastr[icon](msg, title, {
      positionClass: "toast-" + position,
      timeOut: 5000,
      closeButton: true,
      debug: false,
      newestOnTop: true,
      progressBar: true,
      preventDuplicates: true,
      showDuration: 300,
      hideDuration: 1000,
      extendedTimeOut: 1000,
      showEasing: "swing",
      hideEasing: "linear",
      showMethod: "fadeIn",
      hideMethod: "fadeOut",
      tapToDismiss: false,
    });
  });
}

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

function notification_v2(
  title,
  text,
  icon,
  confirmButtonText,
  cancelButtonText,
  confirmCallback
) {
  Swal.fire({
    title: title,
    text: text,
    icon: icon,
    showCancelButton: "true",
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: confirmButtonText,
    cancelButtonText: cancelButtonText,
  }).then((result) => {
    if (result.isConfirmed && typeof confirmCallback === "function") {
      confirmCallback();
    }
  });
}

function initKendoGrid(gridSelector, dataSourceUrl, columns, fields = null, sortField, sortOrder = null, pageSize = 10) {
  $(gridSelector).kendoGrid({
    dataSource: {
      transport: {
        read: {
          url: dataSourceUrl,
          dataType: "json",
          type: "GET",
          contentType: "application/json"
        },
      },
      schema: {
        data: "results",
        total: "count",
        model: {
          fields: fields
        }
      },
      pageSize: pageSize,
      serverPaging: true,
      serverFiltering: true,
      serverSorting: true,
      sort: [{
        field: sortField,
        dir: sortOrder
      }],
      change: function (e) {
        let data = this.data();
        data.forEach(function (item, index) {
          item.index = e.sender.skip() + index + 1;
        });
      },
    },
    columns: columns,
    scrollable: false,
    sortable: true,
    pageable: {
      pageSizes: [10, 25, 50, 100],
      buttonCount: 5,
      refresh: true,
      messages: {
        display: "{0} - {1} จาก {2} รายการ",
        itemsPerPage: "รายการต่อหน้า"
      }
    },
    filterable: true,
    toolbar: ["search", 
      // {
      //   name: "excel",
      //   template: '<button type="button" class="k-grid-excel k-button k-button-md k-rounded-md k-button-solid k-button-solid-base k-icon-button"  data-bs-toggle="tooltip" title="Export to Excel"><span class="k-icon k-i-file-excel k-button-icon"></span></button>'
      // } 
  ],
    // excel: {
    //   fileName: "ex.xlsx",
    //   filterable: true
    // },
    dataBound: function () {

      $("th[data-bs-toggle='tooltip']").each(function () {
        var element = $(this);
        element.kendoTooltip({
          content: element.attr("title"),
          position: "top"
        });
      });

      $('[data-bs-toggle="tooltip"]').each(function () {
        var element = $(this);
        element.kendoTooltip({
          content: element.attr('title'),
          position: "top"
        });
      });

    }
  });
}


function formatRepo(repo) {
  if (repo.loading) return repo.text;
  var name = repo.text;
  return (
    "<div class='select2-result-repository clearfix'>" +
    "<div class='select2-result-repository__meta'>" +
    "<div class='select2-result-repository__title'>" +
    name +
    "</div></div>"
  );
}

function formatRepoSelection(repo) {
  return repo.text;
}

function loadSelect2Data(url, selector, responseKey = null, idKey = null, textKey = null, additionalParams = {}, selectedValue = null, placeholder = '-- เลือกข้อมูล --') {

  let textSelector;
  if (selector == ".js-data-file_type-ajax") {
    textSelector = '-- เลือกประเภทเอกสาร --';
  } else {
    textSelector = '-- เลือกข้อมูล --';
  }

  $(selector).select2({
    width: "100%",
    placeholder: textSelector,
    ajax: {
      url: url,
      dataType: 'json',
      delay: 250,
      data: function (params) {
        return {
          q: params.term,
          page: params.page,
          ...additionalParams
        };
      },
      processResults: function (data, params) {
        params.page = params.page || 1;

        const selectData = data[responseKey].map((item) => {
          let text = item[textKey]; 

          if (selector === ".js-data-branch-ajax") {
            text = item.branch_code + "-" + item.branch_name;
          }

          return {
            id: item[idKey] || item.id,
            text: text,
            value: item.score_type || null,
            name: text  
          };
        });

        return {
          results: selectData,
          pagination: {
            more: (params.page * 30) < data.total_count
          }
        };
      },
      cache: true
    },
    escapeMarkup: function (markup) { return markup; },
    minimumInputLength: 0,
    templateResult: formatRepo,
    templateSelection: formatRepoSelection
  });

  if (selectedValue) {
    $(selector).val(selectedValue).trigger('change');
  }

}

function mathInstallment() {
  let price = parseFloat($("#price").val()) || 0;
  let down_payment = parseFloat($("#down_payment").val()) || 0;

  if (price > 0) {
    $("#down_payment").prop("disabled", false);
  } else {
    $("#down_payment, #interest, #installment, #price_installment").prop("disabled", true);
  }

  if (price > 0 && down_payment > 0) {
    let percent = (down_payment * 100) / price;
    let net_amount = price - down_payment;

    $("#percent").val(percent.toFixed(2));
    $("#net_amount").val(net_amount.toFixed(2));
    $("#interest").prop("disabled", false);
  } else {
    $("#percent, #net_amount").val("0.00");
    $("#interest, #installment, #price_installment").prop("disabled", true);
  }

  calculateInstallment();
}

function calculateInstallment() {
  let net_amount = parseFloat($("#net_amount").val()) || 0;
  let interest_cal = parseFloat($("#interest option:selected").text()) || 0;
  let installment = parseInt($("#installment option:selected").text()) || 0;

  if (interest_cal > 0) {
    $("#installment").prop("disabled", false);
  } else {
    $("#installment, #price_installment").prop("disabled", true);
  }

  if (net_amount > 0 && interest_cal > 0 && installment > 0) {
    interest_cal = interest_cal / 100;
    let installment_price = Math.floor((((net_amount * interest_cal) * installment) + net_amount) / installment);
    $("#price_installment").val(installment_price.toFixed(2));
  } else {
    $("#price_installment").val("");
  }
}


// ฟังก์ชัน datepicker
function datepicker(inputSelector, dateValue = null) {
  // let today = formatDate(new Date());
  // if (dateValue) {
  //   // แปลงปีจาก ค.ศ. เป็น พ.ศ.
  //   let convertedDate = convertToEngDate(dateValue);
  //   if (convertedDate) {
  //     $(inputSelector).val(convertedDate);
  //   }
  // }

  // ฟังก์ชัน datepicker สำหรับวันที่
  $(inputSelector).flatpickr({
    dateFormat: "d/m/Y",
    altInput: true,
    altFormat: "d/m/Y",
    allowInput: true,
    defaultDate: dateValue ,
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
      // แปลงวันที่จาก พ.ศ. เป็น ค.ศ. โดยตรงในเวลาที่เลือก
      // let gregorianDate = convertToThatdate(dateStr);
      let gregorianDate = dateStr;
      $(inputSelector).val(gregorianDate);
      // คำนวณอายุแล้วอัพเดตให้เหมาะสม
      if (inputSelector === "#birthday") {
        calculateAgeFromBirthday(gregorianDate, "#age"); // คำนวณอายุจากวันเกิด
      }
      if (inputSelector === "#start_work") {
        calculateWorkAge(gregorianDate, "#longevity_year", "#longevity_month", "#longevity_day"); // คำนวณอายุงานจากวันที่เริ่มงาน
      }
    }
  });
}

// // ฟังก์ชันแปลงจาก ค.ศ. เป็น พ.ศ.
// function convertToEngDate(dateStr) {
//   let parts = dateStr.split('/');
//   let day = parts[0];
//   let month = parts[1];
//   let year = parseInt(parts[2]);

//   year += 543;

//   return `${day}/${month}/${year}`;
// }

// // ฟังก์ชันแปลงจาก พ.ศ. เป็น ค.ศ.
// function convertToThatdate(dateStr) {
//   let parts = dateStr.split('/');
//   let day = parts[0];
//   let month = parts[1];
//   let year = parseInt(parts[2]);

//   // แปลงปีจาก พ.ศ. เป็น ค.ศ.
//   year -= 543;

//   return `${day}/${month}/${year}`;
// }

// ฟังก์ชันคำนวณอายุ
function calculateAgeFromBirthday(dateStr, outputSelector) {
  let parts = dateStr.split('/');
  let day = parseInt(parts[0], 10);
  let month = parseInt(parts[1], 10) - 1;
  let year = parseInt(parts[2], 10);

  let birthDate = new Date(year, month, day);
  let today = new Date();
  let age = today.getFullYear() - birthDate.getFullYear();

  if (today.getMonth() < birthDate.getMonth() ||
    (today.getMonth() === birthDate.getMonth() && today.getDate() < birthDate.getDate())) {
    age--;
  }

  $(outputSelector).val(age);
  $.ajax({
    url: '/nameList/rangeAge/', 
    type: 'GET',
    dataType: 'json',
    data: {
      "age": age,  // ส่งค่าอายุ
    },
    success: function (response) {
      console.log('Range age data:', response);
      
      // ถ้าตอบกลับมีค่า age_name
      if (response && response.age_name) {
        // เอาค่าที่ได้จาก response มาแสดงใน <select> #customer_age
        $('#customer_age').html(''); // ลบตัวเลือกที่มีอยู่
        $('#customer_age').append('<option value="' + response.id + '">' + response.age_name + '</option>');
      }
    },
    error: function (error) {
      console.error('Error fetching range age:', error);
    }
  });
  
}

function calculateWorkAge(dateStr, yearSelector, monthSelector, daySelector) {
  let parts = dateStr.split('/');
  let day = parseInt(parts[0], 10);
  let month = parseInt(parts[1], 10) - 1;
  let year = parseInt(parts[2], 10);

  let startWorkDate = new Date(year, month, day);
  let today = new Date();

  let years = today.getFullYear() - startWorkDate.getFullYear();
  let months = today.getMonth() - startWorkDate.getMonth();
  let days = today.getDate() - startWorkDate.getDate();

  // ตรวจสอบกรณีที่เดือนปัจจุบันน้อยกว่าเดือนเริ่มงาน
  if (months < 0) {
    years--;
    months += 12;  // ถ้าเดือนน้อยกว่า 0 ให้ปรับปีลงและบวกเดือนให้เป็นบวก
  }

  // ตรวจสอบกรณีวันที่น้อยกว่าที่เริ่มงาน
  if (days < 0) {
    months--;  // ถ้าวันที่น้อยกว่า 0 ให้ปรับเดือนลง
    let lastMonth = new Date(today.getFullYear(), today.getMonth(), 0);  // คำนวณจำนวนวันในเดือนล่าสุด
    days += lastMonth.getDate();  // เพิ่มจำนวนวันของเดือนก่อนหน้าให้ถูกต้อง
  }

  // อัพเดตค่าที่ outputSelector
  $(yearSelector).val(years);  // ปี
  $(monthSelector).val(months);  // เดือน
  $(daySelector).val(days);  // จำนวนวัน
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

function onlyNumberKey(evt) {
  let ASCIICode = evt.which ? evt.which : evt.keyCode;
  return ASCIICode >= 48 && ASCIICode <= 57; // อนุญาตเฉพาะตัวเลข (0-9)
}

function thaiDate() {
  const today = new Date();

  // แปลงปี ค.ศ. เป็นปี พ.ศ.
  const buddhistYear = today.getFullYear() + 543;

  // ดึงวันที่และเดือน
  const day = today.getDate().toString().padStart(2, '0'); // เติมเลข 0 ข้างหน้าหากวันมี 1 หลัก
  const month = (today.getMonth() + 1).toString().padStart(2, '0'); // เดือนเริ่มจาก 0, ต้องบวก 1
  const year = buddhistYear;

  // สร้างวันที่ในรูปแบบ "dd/mm/yyyy"
  return `${day}/${month}/${year}`;
}

function engDate() {
  const today = new Date();
  const buddhistYear = today.getFullYear();


  const day = today.getDate().toString().padStart(2, '0');
  const month = (today.getMonth() + 1).toString().padStart(2, '0'); 1
  const year = buddhistYear;

  return `${day}/${month}/${year}`;
}

function formatDate(dateStr) {
  const date = new Date(dateStr);
  const day = ("0" + date.getDate()).slice(-2);
  const month = ("0" + (date.getMonth() + 1)).slice(-2);
  const year = date.getFullYear();
  return `${day}/${month}/${year}`;
}

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



function changStatus(type, id, dataType,status=null,typeUrl=null,userauth=null) {
  var color = "";
  var tmpTitle = "";

  if (type == "active") {
    color = "#3AC977";
    tmpTitle = "<h3><b>คุณต้องเปิดการใช้งาน <br/> ใช่หรือไม่?</b></h3>";
  } else {
    color = "#FF5E5E";
    tmpTitle = "<h3><b>คุณต้องปิดการใช้งาน <br/> ใช่หรือไม่?</b></h3>";
  }

  Swal.fire({
    title: "",
    html: tmpTitle,
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    cancelButtonText: "ยกเลิก",
    confirmButtonText: "ตกลง",
  }).then((result) => {
    if (result.isConfirmed) {
      $(document).ready(function () {
        var formData = new FormData();
        formData.append("type", typeUrl);
        formData.append("status", status);
        formData.append("id", id);
        formData.append("data_type", dataType);
        formData.append("userauth_id", userauth);

        $.ajax({
          url: urlupdateStatus,
          type: "POST",
          data: formData,
          headers: {
            "X-CSRFToken": getCookie("csrftoken"),
          },
          contentType: false,
          processData: false,
          success: function (response) {
            var data = response;

            if (data.status == "success") {
              $("#status-active-" + id).css("background-color", "");
              $("#status-inactive-" + id).css("background-color", "");
              if (type == "active") {
                $("#status-active-" + id).css("background-color", color);
              } else {
                $("#status-inactive-" + id).css("background-color", color);
              }
              notification("success", "บันทึกสำเร็จ", "success", "ปิด");
            } else {
              notification(
                "แจ้งเตือน",
                "เปลี่ยนสถานะไม่สำเร็จ กรุณาลองใหม่อีกครั้ง",
                "error",
                "ปิด"
              );
            }
          },
        });
      });
    }
  });
}
