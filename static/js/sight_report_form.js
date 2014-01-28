$(document).ready(function () {

  jQuery.fn.center = function () {
    var t = this.parent().position().top - 8;
    var l = this.parent().position().left;
    var parent_pl = parseInt(this.parent().css("padding-left"));
    var parent_pr = parseInt(this.parent().css("padding-right"));
    var parent_width = this.parent().width() + parent_pl + parent_pr;
    var pl = parseInt(this.css("padding-left"));
    var pr = parseInt(this.css("padding-right"));
    var width = this.width() + pl + pr;

    this.css("position","absolute");
    this.css("top", ((this.parent().height() - this.outerHeight()) / 2) + t + "px");
    this.css("left", ((parent_width - width) / 2) + l + parent_pl + pl + parent_pr + pr + "px");
    return this;
  }

  $(".jellyfish_image").click(function () {
    if ($("input[name=specimen_type]:checked").val() == "other") {
      $("#known_specimen_type").prop("checked", true);
    }
    $("." + $(this).attr("class")).removeClass("selected");
    $(this).addClass("selected");

    id = $(this).attr("data-id");
    $("input[name=jellyfish]").val(id);

    info = $("#jellyfish_info");
    $(this).append(info);
    info.hide();
    info.show();
    info.center();
  });

  $("#other_jellyfish input[type=radio]").click(function () {
    if ($(this).is(':checked')) {
      $("#jellyfish_info").hide();
      $(".jellyfish_image").removeClass("selected");
    }
  });

});
