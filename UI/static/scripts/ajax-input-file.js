var acumulador = 0;
var flagData = false;
var flag_porcentaje = false;
var content = {}

var indiceAnterior=null;
var indiceCero=0
var theLink;

var getTH = function () {

   
   
    var indiceActual = $(this).index()
    $(this).css('background', "#02bb8c")
    theLink = $(this).text();
   

    if (indiceAnterior == null) {
       indiceAnterior=indiceActual;      
    }else if (indiceAnterior==indiceActual) {         
       $(this).css('background', "#02bb8c")
       indiceAnterior=indiceActual
    }else if(indiceAnterior!=indiceActual){      
        
        $("th:eq("+ indiceAnterior +")").css('background', "#FFFFFF")
        $(this).css('background', "#02bb8c")
        indiceAnterior=indiceActual
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
            var p = ''
            d2 = document.getElementById(i)
            var newDiv2 = document.createElement('div')
            newDiv2.setAttribute("class", "porcentaje")
            p += (content.porcentaje[i][0] * 100).toFixed(2);

            newDiv2.innerHTML = "<b>Positive: " + p + "%" + "<b/>"
            insertAfter(d2, newDiv2)
            acumulador += parseFloat(p)

            flag_porcentaje = true;
        }

        acumulador = acumulador / content.porcentaje.length
        var negativo = 100 - acumulador
        var lista = [acumulador, negativo]
        console.log('cambio');


        chartt(lista)
        $("#salida").show()
    }
    $("#btncln").click(function () {
        $("#output_file").children().remove();
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
        d = { "formu": new FormData($('#formuu')[0]) };
        $.ajax({
            type: 'POST',
            url: '/process-file',
            data: d['formu'],
            contentType: false,
            cache: false,
            processData: false,
            success: function (d) {
                var content = JSON.parse(d)
                $("#tbl").html(content["contenido"]).show()
                $("th").unbind('click',getTH)
                $("th").click(getTH)
            },
        });
    });

});

$(document).ready(function () {
    function login() {
        $.ajax({
            url: "/process-file2",
            data: $('form').serialize(),
            type: 'POST',
            success: function (response) {

                content = JSON.parse(response)

                var output_file = document.getElementById('output_file')

                if (flagData == false) {
                    for (i = 0; i < content.contenido.length; i++) {
                        var a = ''
                        var divcContent = document.createElement('div')
                        divcContent.setAttribute("id", "n")
                        divcContent.setAttribute("class", "contenido")
                        console.log(divcContent);
                        var newDiv = document.createElement('div')
                        newDiv.setAttribute("id", i)

                        for (z = 0; z < content.contenido[i].length; z++) {
                            a += content.contenido[i][z];
                        }
                        newDiv.innerHTML = a
                        divcContent.appendChild(newDiv)
                        output_file.appendChild(divcContent)
                    }

                    flagData = true;
                    console.log(flagData);
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
        login()
    })
})
let flChart;
function chartt(porcentajes) {
    console.log("fileChart");
    var ctx = document.getElementById('fileChart').getContext("2d");

    if (flChart) {
        flChart.destroy();
    }
    flChart = new Chart(ctx, {

        type: 'doughnut',
        data: {
            labels: ['Positive', 'Negative'],
            datasets: [{
                label: '# of Votes',
                data: porcentajes,
                backgroundColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)'

                ],
                borderColor: [
                    'rgba(255, 99, 132, 0.5)',
                    'rgba(54, 162, 235, 0.5)'

                ],
                circumference: 180,
                rotation: -90,
                borderWidth: 1
            }]
        },

    });
}
