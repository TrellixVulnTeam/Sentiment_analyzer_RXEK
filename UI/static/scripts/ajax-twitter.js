$(document).ready(function () {
    function login() {
        $.ajax({
            url: "/process_twitter",
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
    $("#twitter-text").submit(function (event) {
        event.preventDefault();
        login()
    })
})


