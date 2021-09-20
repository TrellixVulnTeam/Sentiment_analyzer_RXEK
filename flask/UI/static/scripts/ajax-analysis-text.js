$(document).ready(function () {
  selector();
  var dataClean = function () {
    $("input[name='chx']").prop("disabled", false);
    $("#output_main").css({ display: "none" });
    $("#content_text").children().remove();
    $("data_text_per").children().remove();
    $("#btn-send").show();
    $("#btn-cln").css({ display: "none" });
  }
  function textProcessed() {
    $.ajax({
      url: "/process-text-analysis",
      data: $("form").serialize(),
      type: "POST",
      success: function (response) {
        var content = JSON.parse(response);
        $("input[name='chx']").prop("disabled", true);
        $("#content_text").html(content["text"]);
        $("#data_text_per").html((content["text_per"][1] * 100).toFixed(2));
        $("#output_main").show();
        $("#btn-remove").show();
        $("#btn-cln").show();
        $("#btn-send").css({ display: "none" });

        console.log(response);
      },
      error: function (error) {
        console.log(error);
      },
    });

    $("#btn-cln").unbind(dataClean);
    $("#btn-cln").click(dataClean);

    $("#btn-remove").click(function () {
      location.reload();
    });
  }
  $("#analysis-text").submit(function (event) {
    event.preventDefault();
    if (validateText() == true) {
      textProcessed();
    }
  });
});
