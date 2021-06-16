from flask import Flask 
from flask import render_template
from flask import request
import annotated_text as at

from flask import Markup
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')
@app.route("/text-analysis",methods=["GET","POST"])
def text_analysis():
    txt_area =''
    a = ''
 
    if(request.method=='POST'):
        txt_area=request.form.get('text_area',"")
        racismo = request.form.get('racism',"")
        a = at.procesed_text(txt_area)
       
        
    return render_template('text-analysis.html',resultado = a)

@app.route("/file-analysis",methods=["GET","POST"])
def file_analysis():
    name = ''
    a = ''
    if(request.method=='POST'):
        name=request.form.get('columns',"")
        a = at.procesed_csv(name)


 
    return render_template('file-analysis.html',respuesta = Markup(at.dataframe_show()),seleccion =at.d(),res = a)
