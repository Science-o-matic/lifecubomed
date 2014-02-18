var Map = {
  map_id: '#map',

  init: function() {
    var that = this;

    this.map = $(this.map_id);

    this.map.gmap().bind('init', function() {
      that.render();
    });
  },

  render: function(jellyfish_type_id, from_date, to_date) {
    var that = this;

    Api.getSightings(jellyfish_type_id, from_date, to_date, function(data) {
      $.each(data.sightings, function(i, marker) {
        that.map.gmap('addMarker', {
          'position': new google.maps.LatLng(marker.lat, marker.lng),
          'bounds': true
        });
      });
    });
  }
};


var Api = {
  url: '/sightings.json',

  getSightings: function (jellyfish_type_id, from_date, to_date, callback) {
    var params = {}, url = this.url;

    if (jellyfish_type_id) {
      params["jellyfish_type_id"] = jellyfish_type_id;
    }
    if (from_date) {
      params["from_date"] = from_date;
      if (to_date) {
        params["to_date"] = to_date;
      }
    }

    url = this.url;
    if (!$.isEmptyObject(params)) {
      url = this.url + "?" + $.param(params);
    }

    $.getJSON(url, callback);
  }

}

function initTabs() {
  $('ul.tabs').each(function(){
    var $active, $content, $links = $(this).find('a');

    $active = $($links.filter('[href="'+location.hash+'"]')[0] || $links[0]);
    $active.addClass('active');
    $content = $($active.attr('href'));

    $links.not($active).each(function () {
      $($(this).attr('href')).hide();
    });


    $(this).on('click', 'a', function(e){
      $active.removeClass('active');
      $content.hide();

      $active = $(this);
      $content = $($(this).attr('href'));

      $active.addClass('active');
      $content.show();

      e.preventDefault();
    });
  });
}

function renderSightings(jellyfish_type_id, from_date, to_date) {
  if ($(".tabs a[href=#map]").hasClass("active")) {
    Map.render(jellyfish_type_id, from_date, to_date);
  } else {
    renderListSightings(jellyfish_type_id, from_date, to_date);
  }
}

$(document).ready(function () {
  initTabs();
  Map.init();
});
