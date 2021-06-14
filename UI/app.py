from flask import Flask 
from flask import render_template
from flask import request
import annotated_text as at

from flask import Markup
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

@app.route("/file-analysis",methods=["GET","POST"])
def file_analysis():
    df = ''
    df = at.dataframe()
    
    return render_template('f.html',respuesta = Markup(df))
