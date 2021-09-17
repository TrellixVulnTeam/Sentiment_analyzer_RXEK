from UI import app
from flask import json, render_template, request, request
from werkzeug.utils import secure_filename
import os
import pandas as pd
from src import training as t
from UI import twitter_tweepy as tp
from UI import annotated_text as at

app.config['UPLOAD_FOLDER'] = os.path.abspath('UI/tmp')

indexes = []


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/text-analysis")
def render_text_analysis():

    return render_template('text-analysis.html')


@app.route("/process-text-analysis", methods=["POST"])
def process_text_analysis():

    txt_area = request.form['text_area']
    checkbox = request.form['chx']

    content_text = at.procesed_text(txt_area, checkbox)
    percentage = t.classifier(txt_area, at.select_clf(
        checkbox), at.select_BoW_pkl(checkbox))
    data = {"text": content_text, "porcentaje": percentage}

    return json.dumps(data)


@app.route("/file-analysis")
def render_file_analysis():
    at.clearFiles()
    return render_template('file-analysis.html')


@app.route("/process-file-show-table", methods=["POST"])
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

        rows = pd.read_csv(pth)
        data = {"contenido": tabla, "rows": len(rows)}

        with open('ruta.txt', 'w') as f:
            f.write(pth)

    return json.dumps(data)


@app.route("/process-file-analysis", methods=["POST"])
def process_table_header():

    option_mode = 0
    valor = at.openFiles(os.path.abspath("header.txt"))
    ruta = at.openFiles(os.path.abspath("ruta.txt"))
    checkbox = request.form['chx']
    if(indexes == []):
        limit = request.form['n-rows']
        d = at.procesed_csv(ruta, checkbox, valor, limit, option_mode)
        porcentaje = json.loads(at.texto_documento(
            ruta, valor, at.select_clf(checkbox), at.select_BoW_pkl(checkbox), limit))
        porcentaje = porcentaje["porcentaje"]
        indexes.clear()
        data = {"contenido": d, "porcentaje": porcentaje}

    else:
        option_mode = 1

        indexes_order = list(sorted(set(indexes)))

        d = at.procesed_csv(ruta, checkbox, valor, indexes_order, option_mode)
        porcentaje = json.loads(at.texto_documento2(ruta, valor, at.select_clf(
            checkbox), at.select_BoW_pkl(checkbox), indexes_order))
        porcentaje = porcentaje["porcentaje"]
        indexes.clear()
        data = {"contenido": d, "porcentaje": porcentaje}

    return json.dumps(data)


@app.route("/process-file-get-header", methods=["POST"])
def get_header():

    rf = request.form
    for key in rf.keys():
        data = key

    with open('header.txt', 'w') as f:
        f.write(data)
    return data


@app.route("/process-get-index-checkbox", methods=["POST"])
def get_index_checbox():
    indexes.clear()
    rf = request.form
    keys = rf.keys()
    keys = list(keys)[0]

    for i in keys:
        if(i != "]" and i != "[" and i != ","):
            indexes.append(int(i))

    return 'a'


@app.route("/twitter-analysis")
def render_twitter_analysis():

    return render_template('twitter.html')


@app.route("/process_twitter-analysis", methods=["POST"])
def process_twitter():

    input_text = request.form['url_tweet']

    opt = request.form['tags']
    checkbox = request.form['chx']
    data = tp.select_option(opt, input_text)

    if(opt == 'hashtag' or opt == 'user'):
        porcentaje = json.loads(at.texto_twitter(
            data, at.select_clf(checkbox), at.select_BoW_pkl(checkbox)))
        porcentaje = porcentaje["porcentaje"]
        c = at.procesed_tweet(data, checkbox)
    elif(opt == 'url'):
        porcentaje = t.classifier(data, at.select_clf(
            checkbox), at.select_BoW_pkl(checkbox))
        c = at.procesed_text(data, checkbox)
    contenido = {"text": c, "porcentaje": porcentaje, "tag": opt}

    return json.dumps(contenido)
