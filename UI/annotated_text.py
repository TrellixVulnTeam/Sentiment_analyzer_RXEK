import flask
from flask import Markup
import marshal
import pandas as pd


def procesed_text(text, c):
    key_words = deserialize_file()
    color = str(c)    
    text = text.split(' ')
    lista = []
    for i in text:
        if(i in key_words):
            t = Markup('<span class='+color+'>' + i + '</span>')
            lista.append(t)
        else:
            t = Markup('<span class="no-color" >' + i + '</span>')
            lista.append(t)
    return lista


def procesed_csv(path, c):
    if(path != ''):
        key_words = deserialize_file()
        if(c == ''):
            color = 'black'
        else:
            color = str(c)
        df = pd.read_csv(path)
        lista = []
        for row in df['Text'][0:100]:

            text = row.split(' ')

            for i in text:
                if(i in key_words):
                    t = Markup('<span class='+color+'>' + i + '</span>')
                    lista.append(t)
                else:
                    t = Markup('<span class="no-color" >' + i + '</span>')
                    lista.append(t)
            lista.append(Markup('</br>'))

        return lista


def deserialize_file():
    fileIn = open(
        "/home/jules/Documentos/Personal/Sentiment_analyzer/Serialized/binary/Racism.dat", "br")
    dataLoad = marshal.load(fileIn)
    fileIn.close()
    return dataLoad


def dataframe_show(arc):
    if(arc != ''):
        df = pd.read_csv(arc)
        df = df.astype(str).apply(lambda x: x.str.slice(0, 50))
        return df.to_html(max_rows=16, justify='left',index=False)


def d(arc):

    df = pd.read_csv(arc)
    return df.columns
