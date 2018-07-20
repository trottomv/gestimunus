$(".#id_supplier").change(function(){
  var $this = $(this), $clone = $this.clone();
  $this.appendTo("td.field-supplier input");
})(django.JQuery);
