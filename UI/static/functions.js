
function checkFiles(){
  if(document.getElementById("i_csv").files.length != 0){
      alert('a')
  }
}

document.getElementById("i_csv").addEventListener("DOMContentLoaded",checkFiles,false)