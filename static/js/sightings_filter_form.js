$(document).ready(function () {
  $('.date').datepicker();

  $('form#sightings_filter input[type=submit]').click(function() {
    jellyfish_id = $('#jellyfish_id').val();
    from_date = $('#from_date').val();
    to_date = $('#to_date').val();
    renderSightings(jellyfish_id, from_date, to_date);
    return false;
  });
});
