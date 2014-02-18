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

function initMap() {
  map = $('#map');
  map.gmap().bind('init', function() {
    $.getJSON( '/sightings.json', function(data) {
      $.each( data.sightings, function(i, marker) {
        map.gmap('addMarker', {
          'position': new google.maps.LatLng(marker.lat, marker.lng),
          'bounds': true
        });
      });
    });
  });
}

$(document).ready(function () {
  initTabs();
  initMap();
});
