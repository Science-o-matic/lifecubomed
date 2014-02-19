$(document).ready(function () {
  $('input[name=from_date], input[name=to_date]').datepicker();

  $('form#sightings_filter input[type=submit]').click(function() {
    renderSightings();
    return false;
  });
});
