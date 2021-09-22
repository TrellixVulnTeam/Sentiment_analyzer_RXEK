import marshal
from flask import json
import pandas as pd
from nltk.corpus import stopwords
import os
from src import training as t

stop_words = set(stopwords.words("english"))


# Esta funcion recibe un texto procedente del textarea y lo devuelve con las palabras clave coloreadas
def procesed_text(text, c):

    if(text != ''):
        key_words = deserialize_file(c)
        color = str(c)
        text = text.split(' ')

        data = text_colorized(text, key_words, color)

        strA = " ".join(data)
        return strA
# Esta funcion recibe un texto procedente de un tweet y lo devuelve con las palabras clave coloreadas


def procesed_tweet(text, c):

    if(text != ''):
        key_words = deserialize_file(c)
        color = str(c)

        processed_tweet_list = []
        for row in text:

            texto = row.split(' ')

            data = text_colorized(texto, key_words, color)
            processed_tweet_list.append(data)

        return processed_tweet_list

# Esta funcion recibe un texto procedente de un csv y lo devuelve con las palabras clave coloreadas


def procesed_csv(path, c, f, field_index, selector):

    if(path != ''):
        key_words = deserialize_file(c)

        if(c == ''):
            color = 'black'
        else:
            color = str(c)
        df = pd.read_csv(path)

        processed_csv_list = []

        if(selector == 0):
            for row in df[f][:int(field_index)]:

                text = row.split(' ')

                data = text_colorized(text, key_words, color)
                processed_csv_list.append(data)

            return processed_csv_list
        elif(selector == 1):
            for ind in field_index:

                actual_row = df.iloc[ind]
                actual_row = (actual_row[f])

                text = actual_row.split(' ')

                data = text_colorized(text, key_words, color)
                processed_csv_list.append(data)

            return processed_csv_list

 # Devuelve el porcentaje y el texto procesado procedente de las filas  introducidas mediante un campo de texto de un csv


def get_text_csv_nrows(path, f, clasifier, bow, limit):

    if(path != ''):

        df = pd.read_csv(path)
        lista = []
        p = []
        for row in df[f][:int(limit)]:

            lista.append(row)
            p.append(t.classifier(row, clasifier, bow))

        data = {"text": lista, "percent_data": p}

        return json.dumps(data)

 # Devuelve el porcentaje y el texto procesado procedente de las filas  introducidas mediante un campo de texto de un csv


def get_text_csv_index_checkbox(path, f, clasifier, bow, indexes):

    if(path != ''):

        df = pd.read_csv(path)
        lista = []
        p = []

        for ind in indexes:

            actual_row = df.iloc[ind]
            actual_row = (actual_row[f])
            lista = []
            lista.append(actual_row)
            p.append(t.classifier(actual_row, clasifier, bow))
            data = {"text": lista, "percent_data": p}

        return json.dumps(data)

 # Devuelve el porcentaje y el texto procesado procedente de un tweet


def twitter_text(data, clasifier, bow):

    if(data != ''):

        twitter_text_list = []
        p = []
        for row in data:

            twitter_text_list.append(row)
            p.append(t.classifier(row, clasifier, bow))

        data = {"text": twitter_text_list, "twitter_text_per": p}

        return json.dumps(data)

 # Deserializa la bolsa de palabras


def deserialize_file(c):
    x = c
    path_bow = select_BoW(x)
    fileIn = open(path_bow, "br")
    dataLoad = marshal.load(fileIn)
    fileIn.close()
    return dataLoad

# devuelve el dataframe en formato html


def dataframe_show(arc):
    if(arc != ''):
        df = pd.read_csv(arc)
        df = df.astype(str).apply(lambda x: x.str.slice(0, 50))
        return df.to_html(table_id="my-table", classes="pandas", justify='left', index=False)

# devuelve la bolsa de palabras seleccionada en formato dat


def select_BoW(key):

    if(key == 'racism'):
        BoW = os.path.abspath("Serialized/binary/Racism.dat")
    elif(key == 'sexism'):
        BoW = os.path.abspath("Serialized/binary/Sexism.dat")
    return BoW

# devuelve uno de los clasificadores en formato pkl


def select_clf(key):

    if(key == 'racism'):
        clf = os.path.abspath(
            "Serialized/plk/classifiers/racism_clf_.pkl")
    elif(key == 'sexism'):
        clf = os.path.abspath(
            "Serialized/plk/classifiers/sexism_clf_.pkl")
    return clf

# devuelve la bolsa de palabras seleccionada en formato pkl


def select_BoW_pkl(key):

    if(key == 'racism'):
        BoW = os.path.abspath("Serialized/plk/BoW/BoW_Racism.pkl")
    elif(key == 'sexism'):
        BoW = os.path.abspath("Serialized/plk/BoW/BoW_Sexism.pkl")
    return BoW


def openFiles(path):
    f = open(path, 'r')
    data = f.read()
    data = data.replace('"', '')
    return data

# limpia los archivos donde se guarda la ruta del csv y la cabecera seleccionada


def clearFiles():

    f_field = open(os.path.abspath('paths/header.txt'), 'w')
    f_field.write('')
    f_field.close()

    f_path = open(os.path.abspath('paths/path.txt'), 'w')

    f_path.write('')
    f_path.close()

# colorea el texto


def text_colorized(text_data, kw, color):
    list_data_colorized = []
    for i in text_data:

        if(i in kw and i not in stop_words):
            t = '<span class='+color+'>' + i + '</span>'
            list_data_colorized.append(t)
            list_data_colorized.append(' ')
        else:
            t = '<span class="no-color" >' + i + '</span>'
            list_data_colorized.append(t)
            list_data_colorized.append(' ')

    return list_data_colorized
