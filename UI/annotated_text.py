import flask
from flask import Markup
import marshal
import pandas as pd


def annotated_text(*text):

    return text


def procesed_text(text):
    key_words = deserialize_file()

    text = text.split(' ')
    lista = []
    for i in text:
        if(i in key_words):
            t = Markup('<span class="color">' + i + '</span>')
            lista.append(t)
        else:
            t = Markup('<span class="no-color" >' + i + '</span>')
            lista.append(t)
    return lista


def deserialize_file():
    fileIn = open(
        "/home/jules/Documentos/Personal/Sentiment_analyzer/Serialized/binary/Racism.dat", "br")
    dataLoad = marshal.load(fileIn)
    fileIn.close()
    return dataLoad


def dataframe():
    data = pd.DataFrame()

    df = pd.read_csv(
        '/home/jules/Documentos/Personal/Sentiment_analyzer/Data/twitter_sexism_parsed_dataset.csv')
    for i in df.select_dtypes(include=[object]):

        data = df[i].str.slice(0, 20)
    print(data)
    return data



