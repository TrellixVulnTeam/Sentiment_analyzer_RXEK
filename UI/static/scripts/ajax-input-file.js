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
                console.log(response);
                var content = JSON.parse(response)
                $("#texto").html(content["contenido"])

                $("#salida").show()
                $("#analysis").click(function(){
                    $("#output_file").css({"width":"590px","height":"400px"})
                    chart(content["porcentaje"])
                });
                
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
