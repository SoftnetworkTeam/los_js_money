$(document).ready(function () {
  $('#branch').val(branch_id)
  $('#company_id').val(company_id)
  $('#province_save').val(branch_province_id)

  $('#prename').change(function () {
    var prename = $(this).val();
    if (prename === '1') {
      $('#gender').val('M').trigger('change');
    }
    else if (prename === '2' || prename === '3') {
      $('#gender').val('F').trigger('change');
    } else {
      $('#gender').val('').trigger('change');
    }
  });

  loadSelect2Data(urlMasterCustomerPrename, ".js-data-prename-ajax", "results", "id", "pre_name");
  loadSelect2Data(urlMasterOccupation, ".js-data-occup-ajax", "results", "id", "occup_name");
  loadSelect2Data(urlMasterProvince, ".js-data-province-ajax", "results", "id", "province_name");
  loadSelect2Data(urlMasterResidence, ".js-data-residence-ajax", "results", "id", "residence_name");
  loadSelect2Data(urlMasterLivingOwner, ".js-data-living_owner-ajax", "results", "id", "owner_name");
  loadSelect2Data(urlMasterLivingType, ".js-data-living_type-ajax", "results", "id", "type_name");
  loadSelect2Data(urlMasterProvincecurrent, ".js-data-province_current-ajax", "results", "id", "province_name");
  loadSelect2Data(urlMasterResidencecurrent, ".js-data-residence_current-ajax", "results", "id", "residence_name");
  loadSelect2Data(urlMasterLivingOwnercurrent, ".js-data-living_owner_current-ajax", "results", "id", "owner_name");
  loadSelect2Data(urlMasterLivingTypecurrent, ".js-data-living_type_current-ajax", "results", "id", "type_name");
  loadSelect2Data(urlMasterProvinceCompany, ".js-data-company_province-ajax", "results", "id", "province_name");
  loadSelect2Data(urlMasterContractDocument, ".js-data-file_type-ajax", "results", "id", "doc_name");
  loadSelect2Data(urlMasterProvinceSave, ".js-data-province_save-ajax", "results", "id", "province_name");

  loadSelect2Data(urlMastercustomerage, ".js-data-customer_age-ajax", "results", "id", "age_name");
  loadSelect2Data(urlMasterminorchildren, ".js-data-minorchildren-ajax", "results", "id", "children_name");
  loadSelect2Data(urlMastereducationlevel, ".js-data-educationlevel-ajax", "results", "id", "education_name");
  loadSelect2Data(urlBusinesstype, ".js-data-business_type-ajax", "results", "id", "business_type_name");
  loadSelect2Data(urlMastershoptypes, ".js-data-shop_type-ajax", "results", "id", "shop_name");
  loadSelect2Data(urlMasterrentalage, ".js-data-rentalage-ajax", "results", "id", "age_name");
  loadSelect2Data(urlMastermonthlyprofit, ".js-data-monthly_profit-ajax", "results", "id", "profit_name");
  loadSelect2Data(urlMasterbusinessage, ".js-data-business_age-ajax", "results", "id", "age_name");
  loadSelect2Data(urlMastercontractreason, ".js-data-contract_reason-ajax", "results", "id", "reason_name");
  loadSelect2Data(urlinterest, ".js-data-interest-ajax", "results", "id", "interest");
  loadSelect2Data(urlMasterNumberOfInstallment, ".js-data-installment-ajax", "results", "id", "installment_amount");
  loadSelect2Data(urlMastercountry, ".js-data-nation-ajax", "results", "id", "nation_name_th");


  loadAmphoe(province_id);
  function loadAmphoe(province_id) {
    const params = province_id ? { province_id: province_id } : {};
    loadSelect2Data(urlMasterAmphoe && urlMasterAmphoecurrent && urlMasterAmphoeCompany, ".js-data-amphoe-ajax,.js-data-amphoe_current-ajax,.js-data-company_amphoe-ajax", "results", "id", "amphoe_name", params);
  }

  loadTambon(amphoe_id);
  function loadTambon(amphoe_id) {
    const params = amphoe_id ? { amphoe_id: amphoe_id } : {};

    $.ajax({
      url: urlMasterTambon && urlMasterTamboncurrent && urlMasterTambonCompany,
      method: "GET",
      data: params,
      dataType: "json",
      success: function (response) {
        const selectData = response.results.map((item) => ({
          id: item.id,
          text: item.tambon_name,
          postcode: item.postcode,
        }));

        selectData.unshift({ id: "", text: "-- เลือกข้อมูล --" });

        $(".js-data-tambon-ajax").select2({
          data: selectData,
          width: "100%",
        });

        $(".js-data-tambon_current-ajax").select2({
          data: selectData,
          width: "100%",
        });

        $(".js-data-company_tambon-ajax").select2({
          data: selectData,
          width: "100%",
        });

        $(".js-data-tambon-ajax").on("change", function () {
          const selectedTambon = selectData.find((item) => item.id == $(this).val());
          if (selectedTambon) {
            $("#postcode").val(selectedTambon.postcode);
          }
        });

        $(".js-data-tambon_current-ajax").on("change", function () {
          const selectedTambon = selectData.find((item) => item.id == $(this).val());
          if (selectedTambon) {
            $("#postcode_current").val(selectedTambon.postcode);
          }
        });

        $(".js-data-company_tambon-ajax").on("change", function () {
          const selectedTambon = selectData.find((item) => item.id == $(this).val());
          if (selectedTambon) {
            $("#company_postcode").val(selectedTambon.postcode);
          }
        });
      },
    });
  }

  loadBank();
  function loadBank() {
    $(".js-data-bank-ajax").select2({
      width: "100%",
      placeholder: "-- เลือกข้อมูล --",
      ajax: {
        url: urlMasterBank,
        dataType: 'json',
        delay: 250,
        data: function (params) {
          return {
            q: params.term, // search term
            page: params.page,
          };
        },
        processResults: function (data, params) {
          const selectData = data.results.map((item) => ({
            id: item.id,
            text: item.bank_name,
          }));

          params.page = params.page || 1;

          return {
            results: selectData,
            pagination: {
              more: (params.page * 30) < data.total_count // infinite scrolling
            }
          };
        },
        cache: true
      },
      escapeMarkup: function (markup) { return markup; },
      minimumInputLength: 0
    });

    // ถ้ามี customerBankId ให้เลือกธนาคารที่มีอยู่
    if (bank_id) {
      $(".js-data-bank-ajax").val(bank_id).trigger('change');
    }
  }

  $(".js-data-province-ajax").on("change", function () {
    const province_id = $(this).val();
    $(".js-data-amphoe-ajax").val(null).empty();
    $(".js-data-tambon-ajax").val(null).empty();
    $("#postcode").val(null);
    $(".js-data-tambon-ajax").append('<option value="" ><p style="color:#A6A6A6 !important">-- เลือกข้อมูล --</p></option>');
    loadAmphoe(province_id);
  });

  $(".js-data-province_current-ajax").on("change", function () {
    const province_id = $(this).val();
    $(".js-data-amphoe_current-ajax").val(null).empty();
    $(".js-data-tambon_current-ajax").val(null).empty();
    $("#postcode_current").val(null);
    $(".js-data-tambon_current-ajax").append('<option value="" ><p style="color:#A6A6A6 !important">-- เลือกข้อมูล --</p></option>');
    loadAmphoe(province_id);
  });

  $(".js-data-company_province-ajax").on("change", function () {
    const province_id = $(this).val();
    $(".js-data-company_amphoe-ajax").val(null).empty();
    $(".js-data-company_tambon-ajax").val(null).empty();
    $("#postcode_company").val(null);
    $(".js-data-company_tambon-ajax").append('<option value="" ><p style="color:#A6A6A6 !important">-- เลือกข้อมูล --</p></option>');
    loadAmphoe(province_id);
  });

  $(".js-data-amphoe-ajax").on("change", function () {
    const amphoe_id = $(this).val();
    $(".js-data-tambon-ajax").val(null).empty();
    $(".js-data-tambon-ajax").append('<option value="" ><p style="color:#A6A6A6 !important">-- เลือกข้อมูล --</p></option>');
    loadTambon(amphoe_id);
  });


  $(".js-data-amphoe_current-ajax").on("change", function () {
    const amphoe_id = $(this).val();
    $(".js-data-tambon_current-ajax").val(null).empty();
    $(".js-data-tambon_current-ajax").append('<option value="" ><p style="color:#A6A6A6 !important">-- เลือกข้อมูล --</p></option>');
    loadTambon(amphoe_id);
  });

  $(".js-data-company_amphoe-ajax").on("change", function () {
    const amphoe_id = $(this).val();
    $(".js-data-company_tambon-ajax").val(null).empty();
    $(".js-data-company_tambon-ajax").append('<option value="" ><p style="color:#A6A6A6 !important">-- เลือกข้อมูล --</p></option>');
    loadTambon(amphoe_id);
  });

  $(".js-data-tambon-ajax").on("change", function () {
    const selectedOption = $(this).find(":selected");
    const postcode = selectedOption.data("postcode") || "";
    $("#postcode").val(postcode);
  });

  $(".js-data-tambon_current-ajax").on("change", function () {
    const selectedOption = $(this).find(":selected");
    const postcode = selectedOption.data("postcode") || "";
    $("#postcode_current").val(postcode);
  });

  $(".js-data-company_tambon-ajax").on("change", function () {
    const selectedOption = $(this).find(":selected");
    const postcode = selectedOption.data("postcode") || "";
    $("#postcode_company").val(postcode);
  });


  $(".js-data-province_save-ajax").on("change", function () {
    const province_id = $(this).val();
    loadBranches(province_id);
    $(".js-data-branch-ajax").prop("disabled", false);

  });

  loadBranches(province_id);

  function loadBranches(province_id) {
    const params = province_id ? { province_id: province_id } : {};
    loadSelect2Data(urlMasterbranch, ".js-data-branch-ajax", "results", "id", "", params);
  }

  // คำนวณค่าต่างๆ
  // mathInstallment();

  //datepicker
  datepicker("#start_payment", startPaymentDate);
  datepicker("#birthday", birthDate);
  datepicker("#issue_date", issue_date);
  datepicker("#expire_date", expire_date);
  datepicker("#read_card", read_card);
  // datepicker("#start_work", start_work);
  datepicker("#salary_day", salary_day);

  let isSameCardActive = false;
  let originalValues = {};

  // เมื่อเลือก "บันทึกเหมือนที่อยู่ตามทะเบียนบ้าน"
  $("#same_card").on("click", function () {

    let isChecked = $(this).prop("checked");

    $('#address_current').val($('#address').val());

    $('#soi_current').val($('#soi').val());

    $('#road_current').val($('#road').val());

    // $('#living_rental_current').val($('#living_rental').val());

    if (!isSameCardActive) {


      // บันทึกค่าเดิมก่อนเปลี่ยน
      originalValues = {
        province_id: $(".js-data-province_current-ajax").val(),
        province_text: $(".js-data-province_current-ajax option:selected").text(),
        amphoe_id: $(".js-data-amphoe_current-ajax").val(),
        amphoe_text: $(".js-data-amphoe_current-ajax option:selected").text(),
        tambon_id: $(".js-data-tambon_current-ajax").val(),
        tambon_text: $(".js-data-tambon_current-ajax option:selected").text(),
        postcode: $("#postcode_current").val(),

        // residence: $(".js-data-residence_current-ajax").val(),
        // residence_text: $(".js-data-residence_current-ajax option:selected").text(),

        // living_owner: $(".js-data-living_owner_current-ajax").val(),
        // living_owner_text: $(".js-data-living_owner_current-ajax option:selected").text(),

        // living_type: $(".js-data-living_type_current-ajax").val(),
        // living_type_text: $(".js-data-living_type_current-ajax option:selected").text(),
      };

      // ดึงค่าจากที่อยู่ตามบัตร
      let province_id = $(".js-data-province-ajax").val();
      let province_text = $(".js-data-province-ajax option:selected").text();
      let amphoe_id = $(".js-data-amphoe-ajax").val();
      let amphoe_text = $(".js-data-amphoe-ajax option:selected").text();
      let tambon_id = $(".js-data-tambon-ajax").val();
      let tambon_text = $(".js-data-tambon-ajax option:selected").text();
      let postcode = $("#postcode").val();

      // let residence = $(".js-data-residence-ajax").val();
      // let residence_text = $(".js-data-residence-ajax option:selected").text();
      // let living_owner = $(".js-data-living_owner-ajax").val();
      // let living_owner_text = $(".js-data-living_owner-ajax option:selected").text();

      // let living_type = $(".js-data-living_type-ajax").val();
      // let living_type_text = $(".js-data-living_type-ajax option:selected").text();

      // เซ็ตค่าลงใน dropdown ปัจจุบัน
      $(".js-data-province_current-ajax").html(`<option value="${province_id}">${province_text}</option>`).val(province_id);
      $(".js-data-amphoe_current-ajax").html(`<option value="${amphoe_id}">${amphoe_text}</option>`).val(amphoe_id);
      $(".js-data-tambon_current-ajax").html(`<option value="${tambon_id}" data-postcode="${postcode}">${tambon_text}</option>`).val(tambon_id);
      $("#postcode_current").val(postcode);

      // $(".js-data-residence_current-ajax").html(`<option value="${residence}">${residence_text}</option>`).val(residence);
      // $(".js-data-living_owner_current-ajax").html(`<option value="${living_owner}">${living_owner_text}</option>`).val(living_owner);
      // $(".js-data-living_type_current-ajax").html(`<option value="${living_type}">${living_type_text}</option>`).val(living_type);

      loadSelect2Data(urlMasterProvincecurrent, ".js-data-province_current-ajax", "results", "id", "province_name");
      loadAmphoe(province_id);
      loadTambon(amphoe_id);

      loadSelect2Data(urlMasterResidencecurrent, ".js-data-residence_current-ajax", "results", "id", "residence_name");
      loadSelect2Data(urlMasterLivingOwnercurrent, ".js-data-living_owner_current-ajax", "results", "id", "owner_name");
      loadSelect2Data(urlMasterLivingTypecurrent, ".js-data-living_type_current-ajax", "results", "id", "type_name");


      isSameCardActive = true;
      $(this).prop("checked", isChecked);
    } else {

      // คืนค่ากลับเป็นค่าเดิม
      $(".js-data-province_current-ajax").html(`<option value="${originalValues.province_id}">${originalValues.province_text}</option>`).val(originalValues.province_id);
      $(".js-data-amphoe_current-ajax").html(`<option value="${originalValues.amphoe_id}">${originalValues.amphoe_text}</option>`).val(originalValues.amphoe_id);
      $(".js-data-tambon_current-ajax").html(`<option value="${originalValues.tambon_id}" data-postcode="${originalValues.postcode}">${originalValues.tambon_text}</option>`).val(originalValues.tambon_id);
      $("#postcode_current").val(originalValues.postcode);

      // $(".js-data-residence_current-ajax").html(`<option value="${originalValues.residence}">${originalValues.residence_text}</option>`).val(originalValues.residence);

      // $(".js-data-living_owner_current-ajax").html(`<option value="${originalValues.living_owner}">${originalValues.living_owner_text}</option>`).val(originalValues.living_owner);

      // $(".js-data-living_type_current-ajax").html(`<option value="${originalValues.living_type}">${originalValues.living_type_text}</option>`).val(originalValues.living_type);

      loadSelect2Data(urlMasterProvincecurrent, ".js-data-province_current-ajax", "results", "id", "province_name");
      loadAmphoe(province_id);
      loadTambon(amphoe_id);

      loadSelect2Data(urlMasterResidencecurrent, ".js-data-residence_current-ajax", "results", "id", "residence_name");
      loadSelect2Data(urlMasterLivingOwnercurrent, ".js-data-living_owner_current-ajax", "results", "id", "owner_name");
      loadSelect2Data(urlMasterLivingTypecurrent, ".js-data-living_type_current-ajax", "results", "id", "type_name");


      isSameCardActive = false;
      $(this).prop("checked", !isChecked);

    }

  });


});

function selectImg(id) {
  console.log('img id = ', id)
  document.getElementById(id).click();
}

function attachFile(id, editImg = null) {

  var file = $("#" + id)[0].files[0];
  if (!file) return;

  var ext = file.name.split('.').pop().toLowerCase();
  var allowedExtensions = ["pdf", "jpg", "jpeg", "png", "gif"];
  var maxSize = 3 * 1024 * 1024; // 3MB

  if (!allowedExtensions.includes(ext) || file.size > maxSize) {
    notification(
      'แจ้งเตือน',
      'รองรับไฟล์ PDF, JPG, JPEG, PNG, GIF เท่านั้น (ขนาดไม่เกิน 3MB)',
      'warning',
      'ปิด'
    );
    $("#" + id).val('');
    return;
  }

  $(`#view_${id}, #delete_${id}`).prop("disabled", false);

  // แสดงรูปใน img
  if (editImg) {
    var files = document.getElementById(id).files;
    var img = (document.getElementById("img-" + id).src =
      window.URL.createObjectURL(files[0]));
  }
}


function deleteFile(id, editImg = null) {
  $("#" + id).val('');
  $(`#view_${id}, #delete_${id}`).prop("disabled", true);

  if (editImg) {
    document.getElementById("img-" + id).src = "/media/blank-img.jpg";
    document.getElementById(id).value = "";
  }
}
function viewPDF(id, viewEditId = null) {
  var file = $("#" + id)[0].files[0];
  var fileName = viewEditId
  if (file) {
    var ext = file.name.split('.').pop().toLowerCase();
    var reader = new FileReader();

    if (ext === "pdf") {
      reader.onload = function (e) {
        var fileData = e.target.result;
        $("#pdfViewer").attr("src", fileData + "#toolbar=0").css('display', 'block');
        $("#imageViewer").css('display', 'none');
        new bootstrap.Modal($("#previewFile")).show();
      }
      reader.readAsDataURL(file);
    }
    else if (["jpg", "jpeg", "png", "gif"].includes(ext)) {
      reader.onload = function (e) {
        var fileData = e.target.result;
        $("#imageViewer").attr("src", fileData).css('display', 'block');
        $("#pdfViewer").css('display', 'none');
        new bootstrap.Modal($("#previewFile")).show();
      }
      reader.readAsDataURL(file);
    } else {
      notification('แจ้งเตือน', 'รองรับไฟล์ PDF และรูปภาพเท่านั้น', 'warning', 'ปิด');
    }
  }
  else if (fileName) {
    var filePath = "/media/" + fileName;
    var ext = fileName.split('.').pop().toLowerCase();

    if (ext === "pdf") {
      $("#pdfBlank").replaceWith(`
        <object id="pdfBlank" data="${filePath}" type="application/pdf" style="width: 100%; height: 800px; display:block;">
            <p style="font-size: 16;color: #fff;">เบราว์เซอร์ของคุณไม่รองรับการแสดงผล PDF กรุณา <a href="${filePath}" target="_blank">ดาวน์โหลดที่นี่</a></p>
        </object>
    `);
      $("#imageViewer").css('display', 'none');
      new bootstrap.Modal($("#previewFile")).show();
    }
    else if (["jpg", "jpeg", "png", "gif"].includes(ext)) {
      $("#imageViewer").attr("src", filePath).css('display', 'block');
      $("#pdfViewer").css('display', 'none');
      new bootstrap.Modal($("#previewFile")).show();
    } else {
      notification('แจ้งเตือน', 'รองรับไฟล์ PDF และรูปภาพเท่านั้น', 'warning', 'ปิด');
    }
  } else {
    notification('แจ้งเตือน', 'ไม่พบไฟล์', 'warning', 'ปิด');
  }
}


function validateInput(input, length, errorMessage) {
  let regex = /^\d*$/;
  let value = input.value;

  if (!regex.test(value)) {
    input.classList.add('is-invalid');
    input.nextElementSibling.textContent = errorMessage;
  } else {
    input.classList.remove('is-invalid');
  }

  if (value.length > length) {
    input.value = value.slice(0, length);
  }
}

$("#id_dip_chip").click(function () {

  let card_data = JSON.parse('{}');
  // Make a GET request to the API
  $.ajax({
    url: 'http://127.0.0.1:8080/smartcard/data/',
    type: 'GET',
    crossDomain: true,
    dataType: 'json',
    beforeSend: function () {
      kendo.ui.progress($(document.body), true);
    },
    success: function (data) {
      if (JSON.stringify(data) !== '[]') {
        card_data = data;
        if (!jQuery.isEmptyObject(card_data)) {

          $(".js-data-prename-ajax").append('<option value="' + card_data.prename + '" selected>' + card_data.prename + '</option>');
          $("#first_name").val(card_data.fname);
          $("#last_name").val(card_data.lname);
          $("#card_id").val(card_data.cid);
          $("#birthday").val(formatDate(card_data.dob));
          $("#issue_date").val(formatDate(card_data.issue_date));
          $("#expire_date").val(formatDate(card_data.expire_date));
          $("#read_card").val(engDate());

          datepicker("#birthday", formatDate(card_data.dob));
          datepicker("#issue_date", formatDate(card_data.issue_date));
          datepicker("#expire_date", formatDate(card_data.expire_date));
          datepicker("#read_card", engDate());
          calculateAgeFromBirthday(formatDate(card_data.dob), "#age");

          $("#address").val(card_data.address.address1 + ' ' + card_data.address.address2);
          $("#soi").val(card_data.soi);
          $("#road").val(card_data.road);
          $(".js-data-province-ajax").append('<option value="' + card_data.address.province + '" selected>' + card_data.address.province + '</option>');
          $(".js-data-amphoe-ajax").append('<option value="' + card_data.address.amphur + '" selected>' + card_data.address.amphur + '</option>');
          $(".js-data-tambon-ajax").append('<option value="' + card_data.address.tambon + '" selected>' + card_data.address.tambon + '</option>');
          $('#gender').select2();

          if (card_data.prename == 'นาย') {
            $('#gender').val('M').trigger('change');
          } else if (card_data.prename == 'นาง' || card_data.prename == 'นางสาว') {
            $('#gender').val('F').trigger('change');
          }

          $('#address_diffshift').val('true')

          $.ajax({
            url: urlMasterTambon,
            type: 'GET',
            dataType: 'json',
            data: {
              "tambon_name": card_data.address.tambon,
            },
            success: function (data) {
              $("#postcode").val(data.results[0].postcode);
            }
          });



        }
      }
      kendo.ui.progress($(document.body), false);
    },
  });
});

function handleSubmitForm() {
  var form = document.getElementById("myForm");

  Array.prototype.slice.call(form.elements).forEach(function (element) {
    element.addEventListener('input', function () {
      element.classList.remove("is-invalid");
    });
  });

  if (!form.checkValidity()) {
    form.classList.add("was-validated");

    var firstInvalid = form.querySelector(":invalid");
    if (firstInvalid) {
      firstInvalid.scrollIntoView({ behavior: "smooth", block: "center" });
      firstInvalid.classList.add("is-invalid");
      firstInvalid.focus();
    }

    return;
  }

  form.submit();
}

document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("btnSubmit")
    .addEventListener("click", handleSubmitForm);
});

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
    url: urlrangeAge,
    type: 'GET',
    dataType: 'json',
    data: {
      "age": age,
    },
    success: function (response) {

      if (response && response.results && response.results.length > 0) {
        var ageData = response.results[0];

        if (ageData.age_name) {
          $('#customer_age').html('');
          $('#customer_age').append('<option value="' + ageData.id + '" selected>' + ageData.age_name + '</option>');

          $('#customer_age').trigger('change');
        }
      }
    },

  });



}

function validateThaiID(input) {
  let id = input.value;
  let feedback = input.nextElementSibling; 

  if (id.length === 13) {
      if (checkID(id)) {
          input.classList.remove("is-invalid");
          feedback.textContent = "";
      } else {
          input.classList.add("is-invalid");
          feedback.textContent = "กรุณากรอกเลขบัตรประชาชนให้ถูกต้อง";
      }
  } else {
      input.classList.add("is-invalid");
      feedback.textContent = "กรุณากรอกเลขบัตรประชาชนด้วยตัวเลข 13 หลัก";
  }
}

function checkID(id) {
  if (!/^\d{13}$/.test(id)) return false; 
  let sum = 0;
  for (let i = 0; i < 12; i++) {
      sum += parseInt(id.charAt(i)) * (13 - i);
  }
  return (11 - (sum % 11)) % 10 === parseInt(id.charAt(12));
}

function validateEmail(input) {
  let email = input.value.trim();
  let feedback = input.nextElementSibling; 
  let regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

  if (email === "" || regex.test(email)) {
      input.classList.remove("is-invalid");
      feedback.textContent = "";
  } else {
      input.classList.add("is-invalid");
      feedback.textContent = "กรุณากรอกอีเมลให้ถูกต้อง (เช่น example@email.com)";
  }
}
