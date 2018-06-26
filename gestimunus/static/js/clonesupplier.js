$(document).ready(function() {
  var supplier = $("#id_supplier").val();
  console.log(supplier);
  $("td.field-supplier input").each(function() {
    $(this).val(supplier);
    // $(this).css({'background-color' : '#0caa41'});
    // $(this).each(function(index, elem) {
      // supplierdetails = supplier;
    });
    // document.getElementById('id_cashmovementscustomerdetails_set-0-supplier').value=supplier;
    // document.getElementByTagName('td .field-supplier input')[0].value=supplier;
});
