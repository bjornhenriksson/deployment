jQuery(document).ready(function ($) {

    var editor = new MediumEditor('.edit-p');

    $(".js-form").submit(function( event ) {
      event.preventDefault();
      var postid = $(this).data("id");
      var contentObj = $("#desc" + postid).html();
      $("#hidden-desc" + postid).html(contentObj);
      this.submit();
    });

    $(".js-form-new").submit(function( event ) {
      event.preventDefault();
      var contentObj = $("#desc-new").html();
      $("#hidden-desc-new").html(contentObj);
      this.submit();
    });

    $('textarea').autosize();

});   