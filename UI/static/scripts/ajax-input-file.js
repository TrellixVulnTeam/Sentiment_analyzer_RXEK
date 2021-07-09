var acumulador = 0;
var flagData = false;
var flag_porcentaje = false;
var content={}
var fun=function () {
    console.log(document.getElementById("0"))
    if (flag_porcentaje == false) {
        for (i = 0; i < content.porcentaje.length; i++) {
            var p = ''
            d2 = document.getElementById(i)
            var newDiv2 = document.createElement('div')
            newDiv2.setAttribute("class", "porcentaje")
            p += (content.porcentaje[i][0] * 100).toFixed(2);

            newDiv2.innerHTML = "<b>Positive: " + p + "%" + "<b/>"
            d2.appendChild(newDiv2)
            acumulador += parseFloat(p)

            flag_porcentaje = true;
        }
       
        acumulador = acumulador / content.porcentaje.length
        var negativo = 100 - acumulador
        var lista = [acumulador, negativo]
        $("#output_file").css({ "width": "590px", "height": "400px" })
        chart(lista)
    }
    $("#btncln").click(function () {
     $("#output_file").children().remove();
        
        flagData = false;
        flag_porcentaje = false;
        acumulador=0;
        chart(0)
        $("#myChart").css({"display":"none"});
        $("#output_file").css({ "width": "1000px", "height": "600px" })
        
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
                $("th").click(function () {
                    $(this).css('background', "#02bb8c")
                    var theLink = $(this).text();
                    $.ajax({
                        type: "POST",
                        url: '/process-file3',
                        data: JSON.stringify(theLink),
                        dataType: 'json'
                    }).done(function (data) {
                        console.log(data);

                    });



                });
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
                        var newDiv = document.createElement('div')
                        newDiv.setAttribute("id", i)
                        for (z = 0; z < content.contenido[i].length; z++) {
                            a += content.contenido[i][z];
                        }
                        newDiv.innerHTML = a
                        output_file.appendChild(newDiv)
                        flagData = true;
                    }
                    console.log(flagData);
                }

                $("#salida").show()
                var d2;
                $("#analysis").unbind("click",fun)
                $("#analysis").click(fun);


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
let myChart;
function chart(porcentajes) {

    var ctx = document.getElementById('myChart');

    if (myChart) {

        myChart.destroy();
    }
    myChart = new Chart(ctx, {

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

