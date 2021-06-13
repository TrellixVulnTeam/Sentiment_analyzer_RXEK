from flask import Flask 
from flask import render_template
from flask import request
import annotated_text as at
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    txt_area =''
    a = ''
    if(request.method=='POST'):
        txt_area=request.form.get('text_area',"")
        racismo = request.form.get('racism',"")
        a = at.procesed_text(txt_area)
    return render_template('home.html',resultado = a)