
function showName() {
  var filename = $('#i_csv').val().replace(/C:\\fakepath\\/i, '');
  document.getElementById("start").style = "display:none"

  document.getElementById("hdn").style = "display:flex"
  var ext = filename.split(".").pop()
  if (ext == 'csv') {
    document.getElementById("img").innerHTML = '<img src="static/images/i_csv.png"/>'
    document.getElementById("name_f").innerHTML =  "<b>File selected: </b>" + filename
  } 
}
document.getElementById("i_csv").addEventListener('change', checkFiles, false)
function checkFiles() {

  if (document.getElementById("i_csv").files.length != 0) {

    showName();
  }
}
