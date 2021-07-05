$(document).ready(function () {
    function login() {
        $.ajax({
            url: "/process",
            data: $('form').serialize(),
            type: 'POST',
            success: function (response) {
                var content = JSON.parse(response)

                $("#texto").html(content["text"])
                // $("#por_dato").html(content["porcentaje"])
                $("#salida").show()
                chart(content["porcentaje"])
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        });
    }
    $("#analysis-text").submit(function (event) {
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