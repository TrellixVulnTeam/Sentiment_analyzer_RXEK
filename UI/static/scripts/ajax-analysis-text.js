$(document).ready(function () {
    function login() {
        $.ajax({
            url: "/process",
            data: $('form').serialize(),
            type: 'POST',
            success: function (response) {
                var content = JSON.parse(response)

                $("#texto").html(content["text"])
                $("#por_dato").html(((content["porcentaje"][0])*100).toFixed(2))
                $("#salida").show()
               
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


