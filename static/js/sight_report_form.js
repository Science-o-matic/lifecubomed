function Map() {
  this.gmap_id = 'gmap';
  this.map = null;
  this.geocoder = null;
  this.default_lat = 38.84031375122825;
  this.default_lng = 0.11510465294122696;

  this.load = function(lat, lng) {
    this.lat = lat;
    this.lng = lng;

    if (GBrowserIsCompatible()) {
      this.map = new GMap2(document.getElementById(this.gmap_id));
      this.map.addControl(new GSmallMapControl());
      this.map.setMapType(G_SATELLITE_MAP);
      this.map.addControl(new GMapTypeControl());
      this.geocoder = new GClientGeocoder();

      this._setMarker();
/*      GEvent.addListener(
        this.map, "click",
        function(marker, point) {
          if (marker) {
            null;
          } else {
            map.clearOverlays();
            var marcador = new GMarker(point);
            map.addOverlay(marcador);
            document.form_mapa.coordenadas.value = point.y+","+point.x;
          }
        }
      );*/
    }
  };

  this._setMarker = function () {
    this.map.clearOverlays();
    point = new GLatLng(this.lat, this.lng);
    this.map.addOverlay(new GMarker(point));
    this.map.setCenter(new GLatLng(this.lat || this.default_lat, this.lng || this.default_lng),10);
  };

  this.refreshMarker = function(lat, lng) {
    this.lat = lat;
    this.lng = lng;
    this._setMarker();
  };

  this.showAddress = function(address, zoom) {
    if (this.geocoder) {
      this.geocoder.getLatLng(
        address,
        function(point) {
          if (!point) {
            alert(address + " not found");
          } else {
            map.setCenter(point, zoom);
            var marker = new GMarker(point);
            map.addOverlay(marker);
            //marker.openInfoWindowHtml("<b>"+address+"</b><br>Coordenadas:<br>Latitud : "+point.y+"<br>Longitud : "+point.x+"<a href=http://www.mundivideo.com/fotos_pano.htm?lat="+point.y+"&lon="+point.x+"&mapa=3 TARGET=fijo><br><br>Fotografias</a>");
            // marker.openInfoWindowHtml("<b>Coordenadas:</b> "+point.y+","+point.x);
            document.form_mapa.coordenadas.value = point.y+","+point.x;
          }
        }
      );
    }
  };
}

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

$(document).ready(function () {
  map = new Map();

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

  $("#location input").keyup(function () {
    lat = $("input[name=lat]").val();
    lng = $("input[name=lng]").val();
    if ($.isNumeric(lat) && $.isNumeric(lng)) {
      $("#open_gmap").show();
    } else {
      $("#open_gmap").hide();
    }
    if ($("#gmap").is(":visible")) {
      map.refreshMarker(lat, lng);
    }
  });

  $("#open_gmap").click(function () {
    lat = $("input[name=lat]").val();
    lng = $("input[name=lng]").val();
    if (lat && lng) {
      $("#gmap").toggle();
      $("#show_gmap").toggle();
      $("#hide_gmap").toggle();

      src = $("#open_gmap img").attr("src")
      if (src != $("#open_gmap img").attr("data-hide-src")) {
        $("#open_gmap img").attr("src", $("#open_gmap img").attr("data-hide-src"));
      } else {
        $("#open_gmap img").attr("src", $("#open_gmap img").attr("data-show-src"));
      }

      if ($("#gmap").is(":visible")) {
        map.load(lat, lng);
      } else {
        GUnload();
      }
    }
  });

});
