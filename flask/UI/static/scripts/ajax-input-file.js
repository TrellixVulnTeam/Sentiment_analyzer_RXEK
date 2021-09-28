var negativeAcumulator = 0;
var flagData = false;
var flagPercentage = false;
var content = {};
var warning;
var lastIndex = null;
var indexes = [];
var table;
var page;
var flChart;

// Envia mediante ajax cada indice perteneciente a cada checkbox seleccionado
var selectCheckBox = function () {
  let value = table.row(this).index();

  indexes = addOrDeleteElementArray(this, value, indexes,table);
  console.log(indexes);
  $.ajax({
    type: "POST",
    url: "/process-get-index-checkbox",
    data: JSON.stringify(indexes),
    dataType: "json",
  }).done(function (data) {
    console.log(data);
  });
};

var selectAllCheckBoxes = function () {
  page = table.page.info();


  if ($("input.select-checkbox").hasClass("selected")) {
    indexes = deleteAllIndex(page, indexes,table);
    console.log(indexes);
  } else {
    indexes = insertAllIndex(page, table,indexes, this);
    console.log(indexes);
  }
  $.ajax({
    type: "POST",
    url: "/process-get-index-checkbox",
    data: JSON.stringify(indexes),
    dataType: "json",
  }).done(function (data) {
    console.log(data);
  });
};

//Devuelve mediante ajax la cabecera de la tabla
var getTH = function () {
  let actualIndex = $(this).index();
  if (actualIndex != 0) {
    $(this).css("background", "#02bb8c");
    header_field = $(this).text();
    $("#warning").css({ display: "none" });

    lastIndex = changeTH(lastIndex, actualIndex, this);

    $.ajax({
      type: "POST",
      url: "/process-file-get-header",
      data: JSON.stringify(header_field),
      dataType: "json",
    }).done(function (data) {
      console.log(data);
    });
  }
};
//Crea el grafico
function makeFilePercent() {

  if (flagPercentage == false) {
    var returnValue = makeElementPercent("objectPerc", content, flagPercentage, negativeAcumulator);
    flagPercentage = returnValue.flag;

    negativeAcumulator = returnValue.acumul / content.percent_data.length;
    let positive = 100 - negativeAcumulator;
    let percList = [negativeAcumulator, positive];

    flChart = makeChart(percList, "fileChart", flChart);
    $("#output_main").show();
  }


  $("#btn-cln").click(function () {
    dataClean("#output_secondary_file", "#output_main", "#btn-send", "#btn-cln")
    $("#n-rows").val("");
    $("#btnCrearPdf").css({ display: "none" });
    flagData = false;
    flagPercentage = false;
    negativeAcumulator = 0;
    indexes = cleanCheckbox(indexes, table);
    indexes = [];
  });
  //limpia todo el contenido
  $("#btn-remove").click(function () {
    location.reload();
  });
}

//Muestra la tabla que pertenece al dataframe
$(function () {
  $("#i_csv").change(function () {
    $("#tbl").css({ display: "none" })
    $("#anim-loading").show();

    indexes = [];
    d = { nform: new FormData($("#file-form")[0]) };
    $.ajax({
      type: "POST",
      url: "/process-file-show-table",
      data: d["nform"],
      contentType: false,
      cache: false,
      processData: false,
      success: function (d) {
        $("#anim-loading").css({ display: "none" })

        let content = JSON.parse(d);

        $("#warning").html("Select a table header").show();
        $("#tbl").html(content["content-table"]).show();
        //Crea la cabecera para insertar un checkbox que marca el resto de checkbox
        addHeader();
        appendColumn();

        jQuery.moveColumn(
          jQuery("table"),
          $("#my-table tr:last td").length - 1, 0);
        //Propiedades de la tabla con DATATABLES
        $(document).ready(function () {
          table = $(".dataframe").DataTable({
            ordering: false,
            columnDefs: [
              {
                targets: 0,
                data: null,

                defaultContent: "",
                orderable: false,
                className: "select-checkbox",
              },
            ],

            select: {
              style: "multi",
              selector: "td:first-child",
            },
            order: [[1, "asc"]],
          });
          //  $('.dataframe tbody').delegate($("td.select-checkbox").unbind("click", selectCheckBox));
          // ('.dataframe tbody').delegate($("td.select-checkbox").click(selectCheckBox));

          // $("input.select-checkbox").unbind("click", selectAllCheckBoxes);
          // $("input.select-checkbox").click(selectAllCheckBoxes);
          $('.dataframe tbody').on('click', 'td.select-checkbox', function () {
            var value = table.row(this).index();
            indexes = addOrDeleteElementArray(this, value,indexes, table);
            console.log(indexes);
            $.ajax({
              type: "POST",
              url: "/process-get-index-checkbox",
              data: JSON.stringify(indexes),
              dataType: "json",
            }).done(function (data) {
              console.log(data);
            });

          });
          $('.dataframe thead').on('click', 'input.select-checkbox', function () {
            page = table.page.info();


            if ($("input.select-checkbox").hasClass("selected")) {
              indexes = deleteAllIndex(page, indexes,table);
              console.log(indexes);
            } else {
              indexes = insertAllIndex(page, table,indexes, this);
              console.log(indexes);
            }
            $.ajax({
              type: "POST",
              url: "/process-get-index-checkbox",
              data: JSON.stringify(indexes),
              dataType: "json",
            }).done(function (data) {
              console.log(data);
            });

          });

          //informacion que se usa para los checkbox de cada cabecera
          table.on("page.dt", function () {
            let rowsSelected = table
              .rows({ page: "current", selected: true })
              .count();

            checkboxChangePage(rowsSelected);
          });
          //informacion de la pagina actual de la tabla
          table.on("length.dt", function () {
            page = table.page.info();

          });

          $("#number-rows").show();
          $("#num-total-rows").html(content["rows"]);

          $("th").unbind("click", getTH);
          $("th").click(getTH);
        });
      },
    });
  });
});

$(document).ready(function () {
  function processed() {
    indexes = [];
    $.ajax({
      url: "/process-file-analysis",
      data: $("form").serialize(),
      type: "POST",
      success: function (response) {
        content = JSON.parse(response);
        console.log(content);
        let output_file = document.getElementById("output_secondary_file");

        if (flagData == false) {
          makeElementContent(content, output_file);
          flagData = true;
        }
        makeFilePercent();
        $("#btn-remove").show();
        $("#btn-cln").show();
        $("#btn-send").css({ display: "none" });
        $("#btnCrearPdf").show();
      },
      error: function (error) {
        console.log(error);
      },
    });
  }
  $("#file-form").submit(function (event) {
    event.preventDefault();
    validateFile();
    processed();
  });
});
