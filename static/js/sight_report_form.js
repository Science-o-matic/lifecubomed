$(document).ready(function () {

  jQuery.fn.center = function () {
    var t = this.parent().position().top - 4;
    var l = this.parent().position().left;
    var parent_pl = parseInt(this.parent().css("padding-left"));
    var parent_pr = parseInt(this.parent().css("padding-right"));
    var parent_width = this.parent().width() + parent_pl + parent_pr;
    var pl = parseInt(this.css("padding-left"));
    var pr = parseInt(this.css("padding-right"));
    var width = this.width() + pl + pr;

    this.css("position","absolute");
    this.css("top", ((this.parent().height() - this.outerHeight()) / 2) + t + "px");
    this.css("left", ((parent_width - width) / 2) + l + parent_pl + pl + "px");
    return this;
  }

  jQuery.fn.handleJellyFishImageClick = function () {
    if ($("input[name=specimen_type]:checked").val() == "other") {
      $("#known_specimen_type").prop("checked", true);
      $("#other_jellyfish_description").hide();
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
  }

  $('input[name=date]').datepicker();
  $(".jellyfish_image.selected").handleJellyFishImageClick();


  $(".jellyfish_image").click(function () {
    $(this).handleJellyFishImageClick();
  });

  $("input[name=specimen_type]").click(function () {
    if ($(this).val() == 'other') {
      $("#jellyfish_info").hide();
      $(".jellyfish_image").removeClass("selected");
      $("#other_jellyfish_description").show();
    } else {
      $("#other_jellyfish_description").val('');
      $("#other_jellyfish_description").hide();
    }
  });

});
