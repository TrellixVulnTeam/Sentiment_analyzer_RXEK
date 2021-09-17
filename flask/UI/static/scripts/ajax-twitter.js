var acumulador = 0;
var flagData = false;
var flag_porcentaje = false;
var content = {}
var twChart;
var clean = function () {
    $("#output_secondary_twitter").children().remove();
    flagData = false;
    flag_porcentaje = false;
    acumulador = 0;
    
    $("#output_main").css({ "display": "none" });
    $("#twitterChart").css({ "display": "none" })
    $("#output_secondary_twitter").css({ "width": "590px" })
    $("#btn-send").show()
    $("#btncln").css({ "display": "none" });
}

var reload = function () {
    location.reload()
}

function percent() {
    if (flag_porcentaje == false) {
        for (i = 0; i < content.porcentaje.length; i++) {
            var p = ''
            d2 = document.getElementById(i)
            var newDiv2 = document.createElement('div');
            newDiv2.classList.add("class", "porcentaje");
            newDiv2.style.width = "140px";
            p += (content.porcentaje[i][1] * 100).toFixed(2);

            newDiv2.innerHTML = "<b>" + p + "%" + "<b/>"
            d2.appendChild(newDiv2)
            acumulador += parseFloat(p)

            flag_porcentaje = true;
        }

        acumulador = acumulador / content.porcentaje.length
        var positivo = 100 - acumulador
        var lista = [acumulador, positivo]
        console.log('cambio');

        $("#output_main").show()
        twChart=makeChart(lista,"twitterChart",twChart);

    }
    $("#btncln").unbind("click", clean)
    $("#btncln").click(clean)
    $("#btnclear").unbind("click", reload)
    $("#btnclear").click(reload)


}

$(document).ready(function () {
    selector();
    function login() {
        $.ajax({
            url: "/process_twitter-analysis",
            data: $('form').serialize(),
            type: 'POST',
            success: function (response) {

                content = JSON.parse(response)
                console.log(content);
                if (content["tag"] == 'hashtag' || content["tag"] == 'user') {
                    var output_secondary_twitter = document.getElementById('output_secondary_twitter')
                    if (flagData == false) {
                        for (i = 0; i < content.text.length; i++) {
                            var a = ''
                            var divcContent = document.createElement('div')
                            divcContent.setAttribute("id", i)
                            divcContent.setAttribute("class", "contenido")
                            var newDiv = document.createElement('div')
                            newDiv.setAttribute("id", i)
                            for (z = 0; z < content.text[i].length; z++) {
                                a += content.text[i][z];
                            }
                            newDiv.innerHTML = a
                            divcContent.appendChild(newDiv)
                            output_secondary_twitter.appendChild(divcContent)
                            flagData = true;
                        }
                        console.log(flagData);

                        percent()
                        $("#btnclear").show()
                        $("#btncln").show()
                        $("#btn-send").css({ "display": "none" })
                    }
                } else if (content["tag"] == 'url') {

                    var texto = document.createElement('div')

                    var porcen = document.createElement('div')
                    porcen.style.width = "140px"
                    porcen.setAttribute("class", "porcentaje")

                    var union = document.createElement('div')
                    union.setAttribute("class", "content")

                    var output_file = document.getElementById('output_secondary_twitter')
                    texto.innerHTML = content["text"]
                    porcen.innerHTML = "<b>" + ((content["porcentaje"][1]) * 100).toFixed(2) + "% </b> "

                    union.appendChild(texto)
                    union.appendChild(porcen)
                    output_file.appendChild(union)


                    output_file.style.width = "1000px"

                    $("#output_main").show()

                    $("#btnclear").show()
                    $("#btncln").show()
                    $("#btn-send").css({ "display": "none" })
                    $("#btncln").unbind("click", clean)
                    $("#btncln").click(clean)
                    $("#btnclear").unbind("click", reload)
                    $("#btnclear").click(reload)
                }

            },
            error: function (error) {
                console.log(error);
            }
        });
    }
    $("#twitter-text").submit(function (event) {
        event.preventDefault();
        validateTwitter();
        login()
    })
})

