
from flask import Flask, json
from flask import render_template, request, request, jsonify
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


@app.route("/text-analysis")
def show_text_analysis():

    return render_template('text-analysis.html')


@app.route("/process", methods=["POST"])
def pro():

    txt_area = request.form['text_area']
    checkbox = request.form['chx']
    porcentaje = t.classifier(txt_area)
    data = {"text": at.procesed_text(
        txt_area, checkbox), "porcentaje": porcentaje}
    return json.dumps(data)


@app.route("/file-analysis")
def get_file_analysis():

    return render_template('file-analysis.html')


@app.route("/process-file", methods=["POST"])
def process_file():
    filename = ''
    data = ''

    if 'archivo' not in request.files:
        print("errrr")
    else:
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        pth = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(pth)
        tabla = at.dataframe_show(pth)
        cols = str(at.d(pth))
        data = {"tabla": tabla, "columnas": cols}
    return json.dumps(data)


@app.route("/process-file2", methods=["POST"])
def p():
    f=open ('/home/jules/Documentos/Personal/Sentiment_analyzer/UI/mi_fichero.txt','r')
    valor = f.read()
    valor=valor.replace('"','')
    print(valor)
    path = '/home/jules/Documentos/Personal/Sentiment_analyzer/Data/twitter_racism_parsed_dataset.csv'
    checkbox = request.form['chx']
    
    d = at.procesed_csv(path, checkbox, valor)
    return d


@app.route("/process-file3", methods=["POST"])
def pa():
    
    rf = request.form
    for key in rf.keys():
        data = key
        
    with open('mi_fichero.txt', 'w') as f:
        f.write(data)
    return data
