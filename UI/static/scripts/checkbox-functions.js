function addOrDeleteElementArray(sel, value, vector, table) {

    var removed
    if ($(sel).hasClass('selected') == false) {
        console.log("entra if erroneo")
        if ($.inArray(value, vector) == -1) {
            vector.push(value)
            console.log($(sel));
            $(sel).addClass('selected')
        }


        console.log($(sel));
    } else {
        if (table.rows(value, "selected")) {
            $(sel).removeClass('selected')
            console.log("Asdasdasdasdasdasdasd");
            removed = vector.splice(value, 1)
        }
        console.log(removed);
    }

    return vector
}

function deleteAllIndex(vector, page, table) {
    for (p = page.start; p < page.end; p++) {
        table.rows(p).deselect();
        $("input.select-checkbox").removeClass("selected");
        $("td.select-checkbox").removeClass("selected");
        vector.splice(0, 1);

    }
    return vector
}

function insertAllIndex(vector, page, table, ele) {
    for (p = page.start; p < page.end; p++) {
        table.rows(p).select();
        $(ele).addClass("selected");
        let val = table.row(p).index()
        $("td.select-checkbox").addClass("selected");
        if ($.inArray(val, vector) == -1) {
            vector.push(val)
        };
    }
    return vector
}

function checkboxChangePage(rowsSelected) {
    if (rowsSelected == 0) {
        if ($("input.select-checkbox").hasClass("selected") && $("input.select-checkbox").prop('checked', true)) {

            $("input.select-checkbox").removeClass("selected");
            $("input.select-checkbox").prop('checked', false);
        }
    }
    if (rowsSelected != 0) {

        $("input.select-checkbox").addClass("selected");
        $("input.select-checkbox").prop('checked', true);

    }

}

function cleanCheckbox(vector, tbl) {

    if ($("td.select-checkbox").hasClass("selected")) {
        vector = []
        tbl.rows().deselect();
        $("td.select-checkbox").removeClass("selected");
        $("input.select-checkbox").prop('checked', false);
        return vector
    }

}