jQuery(document).ready(function ($) {

    var editor = new MediumEditor('.edit-p');
    $(".js-form").submit(function( event ) {
      event.preventDefault();
      var contentObj = editor.serialize();
      $(".js-content-hidden").val(contentObj['element-0'].value);
      this.submit();
    });

    $('textarea').autosize();

});   