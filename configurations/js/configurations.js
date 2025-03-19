document.addEventListener("DOMContentLoaded", function () {
    console.log('test555665');
});

if (typeUrl == "grade-income") {
    title = "กำหนดข้อมูล เกรดผู้มีรายได้ประจำ";
    $("#title").text(title);
} else if (typeUrl == "grade-unstable") {
    title = "กำหนดข้อมูล เกรดผู้มีรายได้ไม่สม่ำเสมอ";
    $("#title").text(title);
} else if (typeUrl == "scoring") {
    title = "กำหนดข้อมูล การให้คะแนนผู้กู้";
    $("#title").text(title);
}

$(document).ready(function () {
    $("#openDialogButton").kendoButton({
        cssClass: "custom-button",
    });
    // ใช้ JavaScript ในการเปิดใช้งาน tooltip
    var tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
    var tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));


});


async function submitData(btn, id, statusBtn, status_type, status, dataType) {
    var selectedRow = $(btn).closest("tr");

    var formData = new FormData();
    formData.append("id", id);
    formData.append("type_button", statusBtn);
    formData.append("data_type", dataType);

    if (typeUrl == "grade-income" || typeUrl == "grade-unstable") {
        var input_text1 = selectedRow.find("input.form-control.text1").val() || "";
        formData.append("grade_code", input_text1);
    } else {
        var input_text1 = selectedRow.find("input.form-control.text1").val() || "";
        var input_text2 = selectedRow.find("input.form-control.text2").val() || "";
        var input_text3 = selectedRow.find("input.form-control.text3").val() || "";
        var input_text4 = selectedRow.find("input.form-control.text4").val() || "";
        var input_text5 = selectedRow.find("input.form-control.text5").val() || "";

        formData.append("score_name", input_text1);
        formData.append("stable_min", input_text2);
        formData.append("stable_percent", input_text3);
        formData.append("not_stable_min", input_text4);
        formData.append("not_stable_percent", input_text5);
    }

    formData.append("type", status_type);

    try {
        const response = await fetch(urlupdateData, {
            method: 'POST',
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: formData,
        });

        const data = await response.json();

        if (data.status == "save success") {
            notification("success", "บันทึกสำเร็จ", "success", "ปิด");
        } else if (data.status == "delete success") {
            notification("success", "ลบสำเร็จ", "success", "ปิด");
            selectedRow.remove();
        } else if (data.status == "can't delete") {
            notification("แจ้งเตือน", "ไม่สามารถลบข้อมูลหลักได้", "warnning", "ปิด");
        }
    } catch (error) {
        console.error("เกิดข้อผิดพลาด", error);
    }
}

$("#openDialogButton").on("click", function (e) {
    e.preventDefault();
    $("#example tbody tr:contains('ไม่พบข้อมูล')").remove();
    
    let rowCount = $("#example tbody tr").length + 1;
    let newRow = "<tr>";

    newRow += `<td>${rowCount}</td>`;

    if (dataType === "grade") {
        newRow += "<td><input class='form-control input_conf text1' value=''></td>";
    } else {
        newRow += "<td><input class='form-control input_conf text1' style='width: 120px;' value=''></td>";
        newRow += "<td><input class='form-control input_conf text2' value='' onkeypress='return onlyNumberKey(event)'></td>";
        newRow += "<td><input class='form-control input_conf text3' value='' onkeypress='return onlyNumberKey(event)'></td>";
        newRow += "<td><input class='form-control input_conf text4' value='' onkeypress='return onlyNumberKey(event)'></td>";
        newRow += "<td><input class='form-control input_conf text5' value='' onkeypress='return onlyNumberKey(event)'></td>";
        newRow += "<td>ยังไม่ได้บันทึก</td>";
    }

    newRow += `
    <td>
        <div class="d-flex justify-content-between border-0">
            <ul class="nav nav-tabs dzm-tabs" role="tablist" style="background-color: #ebebeb;">
                <li class="nav-item" role="presentation">
                    <button class="nav-link btn btn-success btn-sm" type="button" style="background-color: #3AC977;" >
                        ใช้งาน
                    </button>
                </li>
                <li class="nav-item" role="presentation">
                    <button class="nav-link btn btn-danger btn-sm" type="button">
                        ไม่ใช้งาน
                    </button>
                </li>
            </ul>
        </div>
    </td>`;

    newRow += `
    <td>
        <button type="button" class="btn btn-outline-success btn-sm" data-bs-toggle="tooltip" title="บันทึก" onclick="submitData(this,'','save','${status_type}','A','${dataType}')">
            <i class="fas fa-save"></i>
        </button>
        <button type="button" class="btn btn-outline-danger btn-sm" data-bs-toggle="tooltip" title="ลบ" onclick="removeRow(this)">
            <i class="fas fa-trash"></i>
        </button>
    </td>`;

    newRow += "</tr>";

    $("#example tbody").append(newRow);
    updateRowNumbers();
});

// ฟังก์ชันลบแถว และอัปเดตลำดับใหม่
function removeRow(button) {
    $(button).closest("tr").remove();
    updateRowNumbers();
}

// ฟังก์ชันอัปเดตลำดับของแต่ละแถว
function updateRowNumbers() {
    $("#example tbody tr").each(function (index) {
        $(this).find("td:first").text(index + 1);
    });
}