let image = document.getElementById("image")
images=["static/images/text_analysis.png","static/images/file_analysis.png","static/images/twitter_analysis.png"]
var index =0;
setInterval(()=>{
    image.src=images[index]
    index++;
    if(index==3){
        index=0
    }
},2000)
image.src=images[0]