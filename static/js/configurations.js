  var typeUrl = null;
  if (window.location.pathname.includes("grade-income")) {
    typeUrl = "statusIncome";
    title = "กำหนดข้อมูล เกรดผู้มีรายได้ประจำ";
    $("#title").text(title);
  } else if (window.location.pathname.includes("grade-unstable")) {
    typeUrl = "statusNotIncome";
    title = "กำหนดข้อมูล เกรดผู้มีรายได้ไม่สม่ำเสมอ";
    $("#title").text(title);
  } else if (window.location.pathname.includes("scoring")) {
    typeUrl = "statusScoring";
    title = "กำหนดข้อมูล การให้คะแนนผู้กู้";
    $("#title").text(title);
  }



  urlupdateStatus = "{% url 'configurations:updateStatus' %}";



  var urlupdateData = "{% url 'configurations:updateData' %}";

  function submitData(btn, id, statusBtn, dataType) {
    let typeUrl = "";
    var selectedRow = $(btn).closest("tr");

    var formData = new FormData();
    formData.append("id", id);
    formData.append("type_button", statusBtn);
    formData.append("data_type", dataType);

    if (window.location.pathname.includes("grade-income")) {
      typeUrl = "statusIncome";
      var input_text1 =
        selectedRow.find("input.form-control.text1").val() || "";

      formData.append("grade_code", input_text1);
    } else if (window.location.pathname.includes("grade-unstable")) {
      typeUrl = "statusNotIncome";
      var input_text1 =
        selectedRow.find("input.form-control .text1").val() || "";

      formData.append("grade_code", input_text1);
    } else if (window.location.pathname.includes("scoring")) {
      typeUrl = "statusScoring";
      var input_text1 =
        selectedRow.find("input.form-control.text1").val() || "";
      var input_text2 =
        selectedRow.find("input.form-control.text2").val() || "";
      var input_text3 =
        selectedRow.find("input.form-control.text3").val() || "";
      var input_text4 =
        selectedRow.find("input.form-control.text4").val() || "";
      var input_text5 =
        selectedRow.find("input.form-control.text5").val() || "";

      formData.append("score_name", input_text1);
      formData.append("stable_min", input_text2);
      formData.append("stable_percent", input_text3);
      formData.append("not_stable_min", input_text4);
      formData.append("not_stable_percent", input_text5);
    }

    formData.append("type", typeUrl);

    $.ajax({
      url: urlupdateData,
      type: "POST",
      data: formData,
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
      },
      contentType: false,
      processData: false,
      success: function (response) {
        if (response.status == "save success") {
          notification("success", "บันทึกสำเร็จ", "success", "ปิด");
        } else if (response.status == "delete success") {
          notification("success", "ลบสำเร็จ", "success", "ปิด");
          var grid = $("#grid").data("kendoGrid");
          var dataItem = grid.dataItem(selectedRow);
          grid.dataSource.remove(dataItem);
        }else if (response.status == "can't delete"){
            notification("แจ้งเตือน", "ไม่สามารถลบข้อมูลหลักได้", "warnning", "ปิด");
        }
      },
      error: function (error) {
        console.error("เกิดข้อผิดพลาด", error);
      },
    });
  }

  $("#openDialogButton").on("click", function (e) {
    e.preventDefault();
   
      var grid = $("#grid").data("kendoGrid");
      var dataSource = grid.dataSource;
      var newIndex = dataSource.total() + 1;
  
      var newRow = {
        id: newIndex,
        grade_code: "",
        score_name: "",
        status: "A",
        stable_min: 0,
        stable_percent: 0,
        not_stable_min: 0,
        not_stable_percent: 0,
      };
  
  
      dataSource.add(newRow);

  });