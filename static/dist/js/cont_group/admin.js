jQuery(document).ready(function ($) {
    $('#id_payment_terms').on('change', function (e) {
        var payment_terms = $('#id_payment_terms').val();
        var sequence_method = $("#id_sequence_method");
        var sequence_method_title = $('#select2-id_sequence_method-container');
        if (payment_terms === 'D') {
            sequence_method.val('V');
            sequence_method_title.attr('title', 'ตัดชำระแบบแนวตั้ง');
            sequence_method_title.text('ตัดชำระแบบแนวตั้ง');
        } else {
            sequence_method.val('V');
            sequence_method_title.attr('title', 'ตัดชำระแบบแนวตั้ง');
            sequence_method_title.text('ตัดชำระแบบแนวตั้ง');
        }
    });

});