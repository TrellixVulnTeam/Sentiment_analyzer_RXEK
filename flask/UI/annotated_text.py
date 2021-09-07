import marshal
from flask import json
import pandas as pd
from nltk.corpus import stopwords
import os
from src import training as t

stop_words = set(stopwords.words("english"))


def procesed_text(text, c):
   
    if(text != ''):
        key_words = deserialize_file(c)
        color = str(c)
        text = text.split(' ')

        data = text_colorized(text, key_words, color)

        strA = " ".join(data)
        return strA


def procesed_tweet(text, c):

    if(text != ''):
        key_words = deserialize_file(c)
        color = str(c)

        l = []
        for row in text:

            texto = row.split(' ')

            data = text_colorized(texto, key_words, color)
            l.append(data)

        return l


def procesed_csv(path, c, f, field_index, selector):
    print(selector)
    if(path != ''):
        key_words = deserialize_file(c)

        if(c == ''):
            color = 'black'
        else:
            color = str(c)
        df = pd.read_csv(path)

        l = []

        if(selector == 0):
            for row in df[f][:int(field_index)]:

                text = row.split(' ')

                data = text_colorized(text, key_words, color)
                l.append(data)

            return l
        elif(selector == 1):
            for ind in field_index:

                actual_row = df.iloc[ind]
                actual_row = (actual_row[f])

                text = actual_row.split(' ')

                data = text_colorized(text, key_words, color)
                l.append(data)

            return l


def texto_documento(path, f, clasifier, bow, limit):

    if(path != ''):

        df = pd.read_csv(path)
        lista = []
        p = []
        for row in df[f][:int(limit)]:

            lista.append(row)
            p.append(t.classifier(row, clasifier, bow))

        data = {"text": lista, "porcentaje": p}

        return json.dumps(data)


def texto_documento2(path, f, clasifier, bow, indexes):
    print("indexes texto documento", indexes)
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
            data = {"text": lista, "porcentaje": p}

        return json.dumps(data)


def texto_twitter(data, clasifier, bow):

    if(data != ''):

        lista = []
        p = []
        for row in data:

            lista.append(row)
            p.append(t.classifier(row, clasifier, bow))

        data = {"text": lista, "porcentaje": p}

        return json.dumps(data)


def deserialize_file(c):
    x = c
    path_bow = select_BoW(x)
    fileIn = open(path_bow, "br")
    dataLoad = marshal.load(fileIn)
    fileIn.close()
    return dataLoad


def dataframe_show(arc):
    if(arc != ''):
        df = pd.read_csv(arc)
        df = df.astype(str).apply(lambda x: x.str.slice(0, 50))
        return df.to_html(table_id="my-table", classes="pandas", justify='left', index=False)


def select_BoW(key):

    if(key == 'racism'):
        BoW = os.path.abspath("Serialized/binary/Racism.dat")
    elif(key == 'sexism'):
        BoW = os.path.abspath("Serialized/binary/Sexism.dat")
    print("ruta", BoW)
    return BoW


def select_clf(key):

    if(key == 'racism'):
        clf = os.path.abspath(
            "Serialized/plk/classifiers/racism_clf_.pkl")
    elif(key == 'sexism'):
        clf = os.path.abspath(
            "Serialized/plk/classifiers/sexism_clf_.pkl")
    print("clf", clf)
    return clf


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


def clearFiles():
    
    f_field = open(
        os.path.abspath('mi_fichero.txt'), 'w')
    f_field.write('')
    f_field.close()

    f_path = open(
        os.path.abspath('ruta.txt'), 'w')

    print(f_path)    
    f_path.write('')
    f_path.close()


def text_colorized(text_data, kw, color):
    lista = []
    for i in text_data:

        if(i in kw and i not in stop_words):
            t = '<span class='+color+'>' + i + '</span>'
            lista.append(t)
            lista.append(' ')
        else:
            t = '<span class="no-color" >' + i + '</span>'
            lista.append(t)
            lista.append(' ')

    return lista
