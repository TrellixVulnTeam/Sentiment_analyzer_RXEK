import twitter_tweepy
from flask import Flask, json
from flask import render_template, request, request, jsonify
import annotated_text as at
from werkzeug.utils import secure_filename
import os
import sys
import pandas as pd
sys.path.append('/home/jules/Documentos/Personal/Sentiment_analyzer/src/')
import training as t

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/home/jules/Documentos/Personal/Sentiment_analyzer/tmp'

field=''
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

    porcentaje = t.classifier(txt_area, at.select_clf(
        checkbox), at.select_BoW_pkl(checkbox))
    data = {"text": at.procesed_text(
        txt_area, checkbox), "porcentaje": porcentaje}
    return json.dumps(data)


@app.route("/file-analysis")
def get_file_analysis():
    at.clearFiles()
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
        print(tabla)
        rows=pd.read_csv(pth)        
        data = {"contenido": tabla,"rows":len(rows)}
       
        with open('ruta.txt', 'w') as f:
            f.write(pth)

    return json.dumps(data)


@app.route("/process-file2", methods=["POST"])
def p():
    
    valor = at.openFiles('/home/jules/Documentos/Personal/Sentiment_analyzer/UI/mi_fichero.txt')
    ruta = at.openFiles('/home/jules/Documentos/Personal/Sentiment_analyzer/UI/ruta.txt')  
    checkbox = request.form['chx']
    limit = request.form['n-rows']
    print(limit)
    d = at.procesed_csv(ruta, checkbox, valor,limit)   
    porcentaje = json.loads(at.texto_documento(ruta, valor, at.select_clf(checkbox), at.select_BoW_pkl(checkbox),limit))
    porcentaje = porcentaje["porcentaje"]
    data = {"contenido": d, "porcentaje": porcentaje,"limit":limit}    

    return json.dumps(data)


@app.route("/process-file3", methods=["POST"])
def pa():

    rf = request.form
    for key in rf.keys():
        data = key

    with open('mi_fichero.txt', 'w') as f:
        f.write(data)
    return data


@app.route("/twitter-analysis")
def show_twitter_analysis():

    return render_template('twitter.html')


@app.route("/process_twitter", methods=["POST"])
def process_twitter():

    input_text = request.form['url_tweet']
    
    opt = request.form['tags']
    checkbox = request.form['chx']
    data = twitter_tweepy.select_option(opt, input_text)
  
    if(opt=='hashtag' or opt=='user'):
        porcentaje = json.loads(at.texto_twitter(data, at.select_clf(checkbox), at.select_BoW_pkl(checkbox)))
        porcentaje = porcentaje["porcentaje"]
        c=at.procesed_tweet(data, checkbox)
    elif(opt=='url'):
        porcentaje = t.classifier(data, at.select_clf(checkbox), at.select_BoW_pkl(checkbox))
        c=at.procesed_text(data, checkbox)
    contenido = {"text": c,"porcentaje":porcentaje,"tag":opt}
 
    return json.dumps(contenido)
