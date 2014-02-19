$(document).ready(function () {
  $('input[name=from_date], input[name=to_date]').datepicker();

  $('form#sightings_filter input[type=submit]').click(function() {
    jellyfish_id = $('#id_jellyfish_id').val();
    from_date = $('#id_from_date').val();
    to_date = $('#id_to_date').val();
    renderSightings(jellyfish_id, from_date, to_date);
    return false;
  });
});
