$(document).ready(function () {
  $('.date').datepicker();

  $('form#sightings_filter input[type=submit]').click(function() {
    jellyfish_type_id = $('#jellyfish_type').val();
    from_date = $('#from_date').val();
    to_date = $('#to_date').val();
    renderSightings(jellyfish_type_id, from_date, to_date);
    return false;
  });
});
