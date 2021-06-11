from flask import Flask 
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    txt_area =''
    if(request.method=='POST'):
        txt_area=request.form.get('text_area',"")
        
    return render_template('home.html',resultado = txt_area)