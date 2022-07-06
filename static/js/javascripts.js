$(function() {
  // show the table as soon as the DOM is ready
  //  $("#status_0").attr('hidden', true);
  // $("#status_1").hide();
  // $("#status_2").hide();
  // shows the table on clicking the noted link
   $("#patientType_0").on('click',function() {
    $("input#status_0").hide();
    $("input#status_1").show();
    $("input#status_2").show();
   });
  // hides the table on clicking the noted link
  $("#patientType_1").on('click', function() {
    $("#status_0").show();
    $("#status_1").hide();
    $("#status_2").hide();
    $('#status_0').prop('checked', true).checkboxradio('refresh');
    
   });
  });