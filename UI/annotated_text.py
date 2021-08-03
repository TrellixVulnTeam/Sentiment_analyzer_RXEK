import marshal
from os import path
from zipfile import Path
from flask import json
import pandas as pd
import sys
import nltk
from nltk import data
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
sys.path.append('/home/jules/Documentos/Personal/Sentiment_analyzer/src/')
import training as t

stop_words = set(stopwords.words("english"))


def procesed_text(text, c):

    if(text != ''):
        key_words = deserialize_file(c)
        color = str(c)
        text = text.split(' ')
        lista = []
        for i in text:
            if(i in key_words and i not in stop_words):
                t = '<span class='+color+'>' + i + '</span>'
                lista.append(t)
            else:
                t = '<span class="no-color" >' + i + '</span>'
                lista.append(t)
        strA = " ".join(lista)
        return strA


def procesed_tweet(text, c):

    if(text != ''):
        key_words = deserialize_file(c)
        color = str(c)

        lista = []
        l = []
        for row in text:

            lista = []
            texto = row.split(' ')

            for i in texto:
                if(i in key_words and i not in stop_words):
                    t = '<span class='+color+'>' + i + '</span>'
                    lista.append(t)
                    lista.append(' ')
                else:
                    t = '<span class="no-color" >' + i + '</span>'
                    lista.append(t)
                    lista.append(' ')

            l.append(lista)

        return l


def procesed_csv(path, c, f, limit):
 
    if(path != ''):
        key_words = deserialize_file(c)

        if(c == ''):
            color = 'black'
        else:
            color = str(c)
        df = pd.read_csv(path)

        l = []
        for row in df[f][:int(limit)]:
            
            lista = []
            text = row.split(' ')
            
            for i in text:
                if(i in key_words and i not in stop_words):
                    t = '<span class='+color+'>' + i + '</span>'
                    lista.append(t)
                    lista.append(' ')
                else:
                    t = '<span class="no-color" >' + i + '</span>'
                    lista.append(t)
                    lista.append(' ')

            l.append(lista)

        return l


def procesed_csv2(path, c, f, indexes):

    
    if(path != ''):
        key_words = deserialize_file(c)

        if(c == ''):
            color = 'black'
        else:
            color = str(c)
        df = pd.read_csv(path)

        l = []

        for ind in indexes:

            actual_row = df.iloc[ind]
            actual_row = (actual_row[f])
            lista = []
            text = actual_row.split(' ')
            
            for i in text:
              
                if(i in key_words and i not in stop_words):
                    t = '<span class='+color+'>' + i + '</span>'
                    lista.append(t)
                    lista.append(' ')
                else:
                    t = '<span class="no-color" >' + i + '</span>'
                    lista.append(t)
                    lista.append(' ')

            l.append(lista)

        return l
      

      


# text,clasifier,bow
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


def texto_documento2(path, f, clasifier, bow,indexes):

    if(path != ''):

        df = pd.read_csv(path)
        lista = []
        p = []
        # for row in df[f]:

        #     lista.append(row)
        #     p.append(t.classifier(row, clasifier, bow))

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
        return df.to_html(table_id="my-table",classes="pandas",justify='left', index=False)


def select_BoW(key):

    if(key == 'racism'):
        BoW = "/home/jules/Documentos/Personal/Sentiment_analyzer/Serialized/binary/Racism.dat"
    elif(key == 'sexism'):
        BoW = "/home/jules/Documentos/Personal/Sentiment_analyzer/Serialized/binary/Sexism.dat"

    return BoW


def select_clf(key):

    if(key == 'racism'):
        clf = "/home/jules/Documentos/Personal/Sentiment_analyzer/Serialized/plk/classifiers/racism_clf_.pkl"
    elif(key == 'sexism'):
        clf = "/home/jules/Documentos/Personal/Sentiment_analyzer/Serialized/plk/classifiers/sexism_clf_.pkl"

    return clf


def select_BoW_pkl(key):

    if(key == 'racism'):
        BoW = "/home/jules/Documentos/Personal/Sentiment_analyzer/Serialized/plk/BoW/BoW_Racism.pkl"
    elif(key == 'sexism'):
        BoW = "/home/jules/Documentos/Personal/Sentiment_analyzer/Serialized/plk/BoW/BoW_Sexism.pkl"

    return BoW


def openFiles(path):
    f = open(path, 'r')
    data = f.read()
    data = data.replace('"', '')
    return data


def clearFiles():
    f_field = open(
        '/home/jules/Documentos/Personal/Sentiment_analyzer/UI/mi_fichero.txt', 'w')
    f_field.write('')
    f_field.close()

    f_path = open(
        '/home/jules/Documentos/Personal/Sentiment_analyzer/UI/ruta.txt', 'w')
    f_path.write('')
    f_path.close()
