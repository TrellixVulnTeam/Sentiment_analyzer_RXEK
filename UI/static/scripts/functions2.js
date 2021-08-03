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
    chx.setAttribute("id", "caca")
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

