from flask import Flask
from flask import render_template, request, Markup,jsonify
import annotated_text as at
from werkzeug.utils import secure_filename
import os
import sys
sys.path.append('/home/jules/Documentos/Personal/Sentiment_analyzer/src/')
import training as t

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '/home/jules/Documentos/Personal/Sentiment_analyzer/tmp'


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/text-analysis", methods=["GET"])
def show_text_analysis():
   
    return render_template('text-analysis.html')

@app.route("/text-analysis", methods=["POST"])
def text_analysis():  
  
    txt_area = request.form.get('text_area', "")
    checkbox = request.form.get('chx', "")
    porcentaje = t.classifier(txt_area)
    return render_template('text-analysis.html', resultado=at.procesed_text(txt_area, checkbox),res_p=porcentaje)

@app.route("/file-analysis", methods=["GET"])
def get_file_analysis():   

    return render_template('file-analysis.html')

@app.route("/file-analysis", methods=["POST"])
def file_analysis():
    pth = ''
    checkbox = ''
    if(request.method == 'POST'):
        f = request.files['file']
        checkbox = request.form.get('chx', "")
        filename = secure_filename(f.filename)
        pth = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(pth)
       
    return render_template('file-analysis.html', respuesta=Markup(at.dataframe_show(pth)), res=at.procesed_csv(pth, checkbox))

