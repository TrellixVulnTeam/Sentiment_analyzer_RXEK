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
    th.setAttribute("id", "chx-th")
    var chx_b = document.createElement("input")
    chx_b.setAttribute("type", "checkbox");

    console.log(table.rows)
    th.appendChild(chx_b)
    var row1 = table.rows[0];
    row1.appendChild(th);

}



function createCell(cell, id) {
    console.log(id)

    let ch = document.createElement("INPUT");
    ch.setAttribute("type", "checkbox");
    ch.setAttribute("id", id);
    cell.appendChild(ch);
}

// append column to the HTML table
function appendColumn() {
    let tbl = document.getElementById('my-table'), // table reference
        i;
    // open loop for each row and append cell
    console.log("Adas"+tbl.rows.length);
    for (i = tbl.columns.length; i>=0; i--) {
        createCell(tbl.rows[i].insertCell(tbl.rows[i].cells.length), "chx-row" + i);
    }
}