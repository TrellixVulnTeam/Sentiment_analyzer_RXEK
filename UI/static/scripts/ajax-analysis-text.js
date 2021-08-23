$(document).ready(function () {
   selector();

    function login() {

        $.ajax({
            url: "/process",
            data: $('form').serialize(),
            type: 'POST',
            success: function (response) {
                var content = JSON.parse(response)
                $("input[name='chx']").prop("disabled", true)
                $("#texto").html(content["text"])
                $("#por_dato").html(((content["porcentaje"][1]) * 100).toFixed(2))
                $("#salida").show()
                $("#btnclear").show()
                $("#btncln").show()
                $("#btn-send").css({ "display": "none" })

                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        });
        $("#btncln").click(function () {
            $("input[name='chx']").prop("disabled", false)
            $("#salida").css({ "display": "none" })
            $("#texto").children().remove();
            $("por_dato").children().remove();
            $("#btn-send").show()
            $("#btncln").css({ "display": "none" });

        })
        $("#btnclear").click(function () {
            location.reload()

        })


    }
    $("#analysis-text").submit(function (event) {

        event.preventDefault();
        if (validateText() == true) {
            login()
        }


    })
})

