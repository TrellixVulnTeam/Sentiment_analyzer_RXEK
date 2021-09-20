function showName() {
    let filename = $('#i_csv').val().replace(/C:\\fakepath\\/i, '');
    document.getElementById("start").style = "display:none"

    document.getElementById("hdn").style = "display:flex"
    let ext = filename.split(".").pop()
    if (ext == 'csv') {
        document.getElementById("img").innerHTML = '<img src="static/images/i_csv.png"/>'
        document.getElementById("name_f").innerHTML = "<b>File selected: </b>" + filename
    }
}
document.getElementById("i_csv").addEventListener('change', checkFiles, false)

function checkFiles() {

    if (document.getElementById("i_csv").files.length != 0) {

        showName();
    }
}


// create DIV element and append to the table cell
function addHeader() {
    var table = document.getElementById("my-table");
    var th = document.createElement("th")
    var chx = document.createElement("input")
    chx.setAttribute("type", "checkbox")
    chx.setAttribute("class", "select-checkbox")
    th.appendChild(chx)
    var row1 = table.rows[0];
    row1.appendChild(th);

}



function createCell(cell, id) {

    let ch = document.createElement("div");

    cell.appendChild(ch);
}

// append column to the HTML table
function appendColumn() {
    var tbl = document.getElementById('my-table'), // table reference
        i;
    // open loop for each row and append cell
    for (i = 1; i < tbl.rows.length; i++) {
        createCell(tbl.rows[i].insertCell(tbl.rows[i].cells.length), i, 'chx' + i);
    }
}

var nColumnas = $("#my-table tr:last td").length - 1;

jQuery.moveColumn = function (table, from, to) {
    var rows = jQuery('tr', table);
    var cols;
    rows.each(function () {
        cols = jQuery(this).children('th, td');

        cols.eq(from).detach().insertBefore(cols.eq(to));
    });
}

function changeTH(lastIndex, actualIndex, ele) {

    if (lastIndex == null) {
        lastIndex = actualIndex;

    } else if (lastIndex == actualIndex) {
        $(ele).css('background', "#02bb8c")
        lastIndex = actualIndex

    } else if (lastIndex != actualIndex) {

        $("th:eq(" + lastIndex + ")").css('background', "#FFFFFF")
        $(ele).css('background', "#02bb8c")
        lastIndex = actualIndex

    }
    return lastIndex
}


function makeChart(data, selector, nameChart) {

    let ctx = document.getElementById(selector).getContext("2d");

    if (nameChart) {
        nameChart.destroy();
    }
    nameChart = new Chart(ctx, {

        type: 'doughnut',
        data: {
            labels: ['Yes', 'No'],
            datasets: [{

                data: data,

                backgroundColor: [
                    'rgba(253, 92, 99, 1)',
                    'rgba(0, 193, 110, 1)'

                ],
                hoverOffset: 3,
                borderColor: [
                    'rgba(255, 139, 139, 1)',
                    'rgba(163, 234, 202, 1)'

                ],
                circumference: 180,
                rotation: -90,
                borderWidth: 1
            }]
        },

    });
    return nameChart
}
function dataClean(secondaryContainer, mainContainer, btnS, btnC) {
    $(secondaryContainer).children().remove();
    $(mainContainer).css({ display: "none" });
    $(btnS).show();
    $(btnC).css({ display: "none" });
}
function makeElementPercent(elementID, dataContent, flag, acm) {
    var returnedObject = {};
    console.log(dataContent);
    for (i = 0; i < dataContent.percent_data.length; i++) {
        let aux = ''
        let container = document.getElementById(elementID + i)
        let perDiv = document.createElement('div')
        perDiv.setAttribute("class", "percentage")
        aux += (dataContent.percent_data[i][1] * 100).toFixed(2);

        perDiv.innerHTML = "<b>" + aux + "%" + "<b/>"
        insertAfter(container, perDiv)
        acm += parseFloat(aux)

        flag = true;
    }
    returnedObject["acumul"] = acm;
    returnedObject["flag"] = flag;

    return returnedObject;
}

function makeElementContent(dataContent, output_file) {

    for (i = 0; i < dataContent.data.length; i++) {
        let aux = ''
        let divcContent = document.createElement('div')
        divcContent.setAttribute("id", "content" + i)
        divcContent.setAttribute("class", "cnt")

        let perContainer = document.createElement('div')
        perContainer.setAttribute("id", "objectPerc" + i)

        for (z = 0; z < dataContent.data[i].length; z++) {
            aux += dataContent.data[i][z];
        }
        perContainer.innerHTML = aux
        divcContent.appendChild(perContainer)
        output_file.appendChild(divcContent)
    }

}

function insertAfter(e, i) {
    console.log('e' + e, i);
    if (e.nextSibling) {
        e.parentNode.insertBefore(i, e.nextSibling);
    } else {
        e.parentNode.appendChild(i);
    }
}

function makeElementURLTwitter() {
    var dataText = document.createElement('div')

    var percnt = document.createElement('div')
    percnt.style.width = "140px"
    percnt.setAttribute("class", "percentage")

    var container = document.createElement('div')
    container.setAttribute("class", "content")

    var output_file = document.getElementById('output_secondary_twitter')
    dataText.innerHTML = content["data"]
    percnt.innerHTML = "<b>" + ((content["percent_data"][1]) * 100).toFixed(2) + "% </b> "

    container.appendChild(dataText)
    container.appendChild(percnt)
    output_file.appendChild(container)

    output_file.style.width = "1000px"

}