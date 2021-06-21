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
        print(a )
        
    return render_template('text-analysis.html',resultado = a)

@app.route("/file-analysis",methods=["GET","POST"])
def file_analysis():
    a = ''
    archivos = ''
    if(request.method == 'POST'):
        archivos = request.form.get('files',"")
        a=at.dataframe_show(archivos)

    return render_template('file-analysis.html',respuesta = Markup(a))
