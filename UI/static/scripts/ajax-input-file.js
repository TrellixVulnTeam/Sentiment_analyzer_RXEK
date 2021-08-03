var acumulador = 0;
var flagData = false;
var flag_porcentaje = false;
var content = {}
var warning;
var tabla;
var indiceAnterior = null;
var indiceCero = 0
var theLink;
var indexes = [];
var getTH = function () {

    let indiceActual = $(this).index()
    if (indiceActual != 0) {
        $(this).css('background', "#02bb8c")
        theLink = $(this).text();
        $("#warning").css({ "display": "none" });
        if (indiceAnterior == null) {
            indiceAnterior = indiceActual;
        } else if (indiceAnterior == indiceActual) {
            $(this).css('background', "#02bb8c")
            indiceAnterior = indiceActual
        } else if (indiceAnterior != indiceActual) {

            $("th:eq(" + indiceAnterior + ")").css('background', "#FFFFFF")
            $(this).css('background', "#02bb8c")
            indiceAnterior = indiceActual
        }

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



function insertAfter(e, i) {
    console.log('e' + e, i);
    if (e.nextSibling) {
        e.parentNode.insertBefore(i, e.nextSibling);
    } else {
        e.parentNode.appendChild(i);
    }
}

function percentt() {

    if (flag_porcentaje == false) {
        for (i = 0; i < content.porcentaje.length; i++) {
            let p = ''
            let d2 = document.getElementById("porcentaje" + i)
            let newDiv2 = document.createElement('div')
            newDiv2.setAttribute("class", "porcentaje")
            p += (content.porcentaje[i][1] * 100).toFixed(2);

            newDiv2.innerHTML = "<b>" + p + "%" + "<b/>"
            insertAfter(d2, newDiv2)
            acumulador += parseFloat(p)

            flag_porcentaje = true;
        }

        acumulador = acumulador / content.porcentaje.length
        let positivo = 100 - acumulador
        let lista = [acumulador, positivo]


        chartt(lista)
        $("#salida").show()
    }
    $("#btncln").click(function () {
        $("#output_file").children().remove();
        $("#n-rows").val('')
        flagData = false;
        flag_porcentaje = false;
        acumulador = 0;
        chart(0)

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

                var nColumnas = $("#my-table tr:last td").length - 1;
                var tbl = jQuery('table');
                jQuery.moveColumn(tbl, nColumnas, 0);

                var table = $('.dataframe').DataTable({
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


                table.on("click", "th.select-checkbox", function () {
                    var page = table.page.info();

                    if ($("th.select-checkbox").hasClass("selected")) {

                        for (p = page.start; p < page.end; p++) {
                            table.rows(p).deselect();
                            $("th.select-checkbox").removeClass("selected");
                            let value = table.row(p).index()
                            
                            console.log(value);
                            if ($.inArray(value, indexes) != -1) {
                                indexes.pop(value)
                            };

                        }
                    } else {
                        for (p = page.start; p < page.end; p++) {
                            table.rows(p).select();
                            $("th.select-checkbox").addClass("selected");
                            let value = table.row(p).index()
                            
                            console.log(value);
                            if ($.inArray(value, indexes) == -1) {
                                indexes.push(value)
                            };
                        }
                    }
                    $.ajax({
                        type: "POST",
                        url: '/process-file4',
                        data: JSON.stringify(indexes),
                        dataType: 'json'
                    }).done(function (data) {
                        console.log(data);

                    });
                })

                table.on('page.dt', function () {
                    let selected = table.rows({ page: 'current', selected: true }).count()
                    console.log(selected);
                    if (selected == 0) {
                        if ($("th.select-checkbox").hasClass("selected") && $("input.select-checkbox").prop('checked', true)) {

                            $("th.select-checkbox").removeClass("selected");
                            $("input.select-checkbox").prop('checked', false);
                        }
                    }
                    if (selected != 0) {

                        $("th.select-checkbox").addClass("selected");
                        $("input.select-checkbox").prop('checked', true);

                    }



                });

                // $('.dataframe tbody').on('click', '.select-checkbox', function () {
                //     let value = table.row(this).index()

                //     $.ajax({
                //         type: "POST",
                //         url: '/process-file4',
                //         data: JSON.stringify(indexes),
                //         dataType: 'json'
                //     }).done(function (data) {
                //         console.log(data);

                //     });
                // });





                $("#number-rows").show();
                $("#num-total-rows").html(content["rows"]);

                $("th").unbind('click', getTH);
                $("th").click(getTH);



            },
        });
    });

});

$(document).ready(function () {
    selector();

    function login() {

        $.ajax({
            url: "/process-file2",
            data: $('form').serialize(),
            type: 'POST',
            success: function (response) {

                content = JSON.parse(response)
                console.log(content);
                let output_file = document.getElementById('output_file')

                if (flagData == false) {
                    for (i = 0; i < content.contenido.length; i++) {
                        let a = ''
                        let divcContent = document.createElement('div')
                        divcContent.setAttribute("id", "content" + i)
                        divcContent.setAttribute("class", "contenido")

                        let newDiv = document.createElement('div')
                        newDiv.setAttribute("id", "porcentaje" + i)

                        for (z = 0; z < content.contenido[i].length; z++) {
                            a += content.contenido[i][z];
                        }
                        newDiv.innerHTML = a
                        divcContent.appendChild(newDiv)
                        output_file.appendChild(divcContent)
                    }

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
let flChart;

function chartt(porcentajes) {

    let ctx = document.getElementById('fileChart').getContext("2d");

    if (flChart) {
        flChart.destroy();
    }
    flChart = new Chart(ctx, {

        type: 'doughnut',
        data: {
            labels: ['Yes', 'No'],
            datasets: [{
                label: '# of Votes',
                data: porcentajes,

                backgroundColor: [
                    'rgba(255, 139, 139, 1)',
                    'rgba(163, 234, 202, 1)'

                ],
                hoverOffset: 6,
                borderColor: [
                    'rgba(255, 139, 139, 1)',
                    'rgba(163, 234, 202, 1)'

                ],
                circumference: 180,
                rotation: -90,
                borderWidth: 1
            }]
        },

    });
}