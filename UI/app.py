from flask import Flask, json
from flask import render_template, request, request, jsonify
import annotated_text as at
from werkzeug.utils import secure_filename
import os
import sys
sys.path.append('/home/jules/Documentos/Personal/Sentiment_analyzer/src/')
import training as t
import PyPDF2
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
    
    porcentaje = t.classifier(txt_area,at.select_clf(checkbox),at.select_BoW_pkl(checkbox))
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
        ext =pth.split('.').pop()
        f.save(pth)
        if(ext =='csv'):
            tabla = at.dataframe_show(pth)
            data = {"contenido": tabla}
        elif(ext=='pdf'):
            reader = PyPDF2.PdfFileReader(pth)

            page = reader.getPage(0)
            pdfDat = page.extractText()
            data = {"contenido": pdfDat}
        with open('ruta.txt', 'w') as f:
            f.write(pth)
       
       
    return json.dumps(data)


@app.route("/process-file2", methods=["POST"])
def p():
   
    valor=at.openFiles('/home/jules/Documentos/Personal/Sentiment_analyzer/UI/mi_fichero.txt')
    ruta=at.openFiles('/home/jules/Documentos/Personal/Sentiment_analyzer/UI/ruta.txt')
    ext=ruta.split('.').pop()
    
    checkbox = request.form['chx']
    if(ext =='csv'):
        d = at.procesed_csv(ruta, checkbox, valor)
        porcentaje=t.classifier(at.texto_documento(ruta,valor),at.select_clf(checkbox),at.select_BoW_pkl(checkbox))
        # porcentaje=at.texto_documento(ruta,valor,at.select_clf(checkbox),at.select_BoW_pkl(checkbox))
        data = {"contenido": d,"porcentaje":porcentaje}
    elif(ext =='pdf'):
        reader = PyPDF2.PdfFileReader(ruta)
        page = reader.getPage(0)
        pdfDat = page.extractText()
        d=at.procesed_text(pdfDat,checkbox)
        porcentaje=at.texto_documento(ruta,valor,at.select_clf(checkbox),at.select_BoW_pkl(checkbox))
        
        data = {"contenido": d,"porcentaje":[10,90]}
    return json.dumps(data)


@app.route("/process-file3", methods=["POST"])
def pa():
    
    rf = request.form
    for key in rf.keys():
        data = key
        
    with open('mi_fichero.txt', 'w') as f:
        f.write(data)
    return data


