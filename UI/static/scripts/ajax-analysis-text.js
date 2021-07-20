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
            $("#salida").css({"display": "none"})
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
        login()
    })
})


