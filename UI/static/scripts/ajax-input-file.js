var acumulador = 0;
var flagData = false;
var flag_porcentaje = false;
var content = {}
var warning;
var indiceAnterior = null;
var theLink;
var indexes = [];
var table;
var page;
var flChart;


var selectCheckBox = function () {
    let value = table.row(this).index()

    dddd = addOrDeleteElementArray(this, value, indexes, table)
    console.log(dddd)
    $.ajax({
        type: "POST",
        url: '/process-file4',
        data: JSON.stringify(dddd),
        dataType: 'json'
    }).done(function (data) {
        console.log(data);

    });
}

var selectAllCheckBoxes = function () {
    
    page = table.page.info();
    var dddd;
    console.log("entraaaos");

    if ($("input.select-checkbox").hasClass("selected")) {

        dddd = deleteAllIndex(indexes, page, table)
    } else {

        dddd = insertAllIndex(indexes, page, table, this)
        console.log(dddd)
    }
    $.ajax({
        type: "POST",
        url: '/process-file4',
        data: JSON.stringify(dddd),
        dataType: 'json'
    }).done(function (data) {
        console.log(data);

    });
}

var getTH = function () {

    let indiceActual = $(this).index()
    if (indiceActual != 0) {

        $(this).css('background', "#02bb8c")
        theLink = $(this).text();
        $("#warning").css({ "display": "none" });

        indiceAnterior = changeTH(indiceAnterior, indiceActual, this)

        $.ajax({
            type: "POST",
            url: '/process-file3',
            data: JSON.stringify(theLink),
            dataType: 'json'
        }).done(function (data) {
            console.log(data);

        });
    }
}


function percentt() {
    console.log("p" + indexes);
    if (flag_porcentaje == false) {

        var returnValue = makeElementPercent("porcentaje", content, flag_porcentaje, acumulador)
        flag_porcentaje = returnValue.flag;

        acumulador = returnValue.acumulador / content.porcentaje.length
        let positivo = 100 - acumulador
        let lista = [acumulador, positivo]

        flChart = makeChart(lista, 'fileChart', flChart)
        $("#salida").show()
    }
    $("#btncln").click(function () {
        $("#output_file").children().remove();
        $("#n-rows").val('')
        flagData = false;
        flag_porcentaje = false;
        acumulador = 0;
        indexes = cleanCheckbox(indexes, table)

        $("#salida").css({ "display": "none" });
        $("#btn-send").show()
        $("#btncln").css({ "display": "none" });

    })
    $("#btnclear").click(function () {
        location.reload()

    })


}
$(function () {
    $('#i_csv').change(function () {
        indexes = []
        d = { "formu": new FormData($('#formuu')[0]) };
        $.ajax({
            type: 'POST',
            url: '/process-file',
            data: d['formu'],
            contentType: false,
            cache: false,
            processData: false,
            success: function (d) {
                let content = JSON.parse(d);

                $("#warning").html("Select a table header").show();
                $("#tbl").html(content["contenido"]).show();

                addHeader()
                appendColumn()

                jQuery.moveColumn(jQuery('table'), $("#my-table tr:last td").length - 1, 0);

                table = $('.dataframe').DataTable({
                    "ordering": false,
                    columnDefs: [{
                        targets: 0,
                        data: null,

                        defaultContent: '',
                        orderable: false,
                        className: 'select-checkbox',

                    }],

                    select: {
                        style: 'multi',
                        selector: 'td:first-child'
                    },
                    order: [[1, 'asc']]

                });


                $("input.select-checkbox").unbind('click', selectAllCheckBoxes);
                $('input.select-checkbox').click(selectAllCheckBoxes)

                table.on('page.dt', function () {
                    let rowsSelected = table.rows({ page: 'current', selected: true }).count()

                    checkboxChangePage(rowsSelected);

                });

                table.on( 'length.dt', function (  ) {
                    
                    page = table.page.info();
                    console.log(page);
                } );
                $("td.select-checkbox").unbind('click', selectCheckBox);
                $('td.select-checkbox').click(selectCheckBox)



                $("#number-rows").show();
                $("#num-total-rows").html(content["rows"]);

                $("th").unbind('click', getTH);
                $("th").click(getTH);

            },
        });
    });

});

$(document).ready(function () {

    function login() {
        indexes = []
        $.ajax({
            url: "/process-file2",
            data: $('form').serialize(),
            type: 'POST',
            success: function (response) {

                content = JSON.parse(response)

                let output_file = document.getElementById('output_file')

                if (flagData == false) {

                    makeElementContent(content, output_file)
                    flagData = true;

                }
                percentt()
                $("#btnclear").show()
                $("#btncln").show()
                $("#btn-send").css({ "display": "none" })

            },
            error: function (error) {
                console.log(error);
            }
        });
    }
    $("#formuu").submit(function (event) {
        event.preventDefault();
        validateFile()
        login()
    })
})
