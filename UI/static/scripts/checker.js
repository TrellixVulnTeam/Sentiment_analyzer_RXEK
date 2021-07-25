
var checkboxRacism = document.getElementById("racism")
var checkboxSexism = document.getElementById("sexism")
var selectores = document.getElementById("selectores")

function validateText() {

    var txt = document.getElementById("text_area")
    var validText = false;
    var validSelector = false

    if (txt.value.length == 0) {

        txt.style.border = "1px solid red";
        alert("You must write a text to analyze")
        validText = false;
    } else {
        txt.style.border = "1px solid rgb(202, 202, 202)";
        validText = true;
    }

    if (!checkboxRacism.checked && !checkboxSexism.checked) {

        selectores.style.border = "1px solid red";
        alert("You must select one of the options")
        validSelector = false;
    } else {
        selectores.style.border = "2px solid rgb(202, 202, 202)";
        validSelector = true;
    }

    if (validText == true && validSelector == true) {
        return true
    } else {
        return false
    }
}

function validateFile() {

    var fileDrag = document.getElementById("file-drag")
    var inputFile = document.getElementById("i_csv")
    var validFile = false;
    var validSelector = false

    if (inputFile.files.length == 0) {
        console.log("entra")
        fileDrag.style.border = "1px solid red";
        validFile = false;
    } else {
        fileDrag.style.border = "2px solid rgb(202, 202, 202)";
        validFile = true;
    }

    if (!checkboxRacism.checked && !checkboxSexism.checked) {

        selectores.style.border = "1px solid red";
        validSelector = false;

    } else {
        selectores.style.border = "2px solid rgb(202, 202, 202)";
        validSelector = true;
    }

    if (validFile == true && validSelector == true) {
        return true
    } else {
        return false
    }
}


function validateTwitter() {

    var inputTweet = document.getElementById("url_tweet")
    var validInput = false;
    var validSelector = false

    if (inputTweet.value.length == 0 || inputTweet.value == ' ') {

        inputTweet.style.border = "1px solid red";
        validInput = false;
    } else {
        inputTweet.style.border = "1px solid rgb(202, 202, 202)";
        validInput = true;
    }

    if (!checkboxRacism.checked && !checkboxSexism.checked) {

        selectores.style.border = "1px solid red";
        validSelector = false;
    } else {
        selectores.style.border = "2px solid rgb(202, 202, 202)";
        validSelector = true;
    }
    if (validInput == true && validSelector == true) {
        return true
    } else {
        return false
    }
}

function selector() {
       
    $(document).on('click', '.checks', function () {

        //Revisa en que status está el checkbox y controlalo según lo //desees
        let val = $(this).attr("id")
        console.log((val));
        if (val == "racism") {
            console.log("entra");
            $("#sexism").prop("checked", false);

        }
        
        if (val == "sexism") {
            console.log("entra2");
            $("#racism").prop("checked", false);

        }

    });

}