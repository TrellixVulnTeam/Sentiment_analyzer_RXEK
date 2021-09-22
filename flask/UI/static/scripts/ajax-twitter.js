var negativeAcumulator = 0;
var flagData = false;
var flagPercentage = false;
var content = {}
var twChart;

var clean = function () {
    dataClean("#output_secondary_twitter", "#output_main", "#btn-send", "#btn-cln")
     var output_secondary_twitter = document.getElementById('output_secondary_twitter')
     output_secondary_twitter.style.width =  "590px";
    flagData = false;
    flagPercentage = false;
    negativeAcumulator = 0;
 $("#btnCrearPdf").css({ display: "none" });
}

var reload = function () {
    location.reload()
}

function makeTwitterPercent() {
    if (flagPercentage == false) {        
        var returnValue = makeElementPercent("objectPerc", content, flagPercentage, negativeAcumulator);
        flagPercentage = returnValue.flag;

        negativeAcumulator = returnValue.acumul / content.percent_data.length;
        let positive = 100 - negativeAcumulator;
        let percList = [negativeAcumulator, positive];

        $("#output_main").show()
        twChart = makeChart(percList, "twitterChart", twChart);

$(".chart-container").show();
    }
    $("#btn-cln").unbind("click", clean)
    $("#btn-cln").click(clean)
    $("#btn-remove").unbind("click", reload)
    $("#btn-remove").click(reload)


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
                        makeElementContent(content, output_secondary_twitter);
                        flagData = true;
                    }
                    makeTwitterPercent()

                    $("#btn-remove").show()
                    $("#btn-cln").show()
                    $("#btn-send").css({ "display": "none" })
                    $("#btnCrearPdf").show();

                } else if (content["tag"] == 'url') {

                    makeElementURLTwitter();

                    $("#output_main").show()

                    $("#btn-remove").show()
                    $("#btn-cln").show()
                    $("#btn-send").css({ "display": "none" })
                    $("#btn-cln").unbind("click", clean)
                    $("#btn-cln").click(clean)
                    $("#btn-remove").unbind("click", reload)
                    $("#btn-remove").click(reload)
                    $("#btnCrearPdf").show();
                    $(".chart-container").css({ "display": "none" })
                    
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

