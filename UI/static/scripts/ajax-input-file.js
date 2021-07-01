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
                $("#tbl").html(content["tabla"])
                document.querySelector('th').addEventListener('click', function () {
                    alert("hola")
                  
                })
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

                $("#texto").html(response)
                $("#salida").show()
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