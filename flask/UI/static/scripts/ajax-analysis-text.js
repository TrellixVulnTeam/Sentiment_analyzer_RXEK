$(document).ready(function () {
  selector();

  function login() {
    $.ajax({
      url: "/process-text-analysis",
      data: $("form").serialize(),
      type: "POST",
      success: function (response) {
        var content = JSON.parse(response);
        $("input[name='chx']").prop("disabled", true);
        $("#content_text").html(content["text"]);
        $("#por_dato").html((content["porcentaje"][1] * 100).toFixed(2));
        $("#output_main").show();
        $("#btnclear").show();
        $("#btncln").show();
        $("#btn-send").css({ display: "none" });

        console.log(response);
      },
      error: function (error) {
        console.log(error);
      },
    });
    $("#btncln").click(function () {
      $("input[name='chx']").prop("disabled", false);
      $("#output_main").css({ display: "none" });
      $("#content_text").children().remove();
      $("por_dato").children().remove();
      $("#btn-send").show();
      $("#btncln").css({ display: "none" });
    });
    $("#btnclear").click(function () {
      location.reload();
    });
  }
  $("#analysis-text").submit(function (event) {
    event.preventDefault();
    if (validateText() == true) {
      login();
    }
  });
});
