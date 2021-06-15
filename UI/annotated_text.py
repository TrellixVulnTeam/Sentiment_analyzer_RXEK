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

def procesed_csv(nombre):
    key_words = deserialize_file()
    df = pd.read_csv(
        '/home/jules/Documentos/Personal/Sentiment_analyzer/Data/twitter_sexism_parsed_dataset.csv')
    lista = []
    for row in df[nombre]:
       
        text = row.split(' ')
        
        
        for i in text:
            if(i in key_words):
                t = Markup('<span class="color">' + i + '</span>')
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


def dataframe_show():
   
    df = pd.read_csv(
        '/home/jules/Documentos/Personal/Sentiment_analyzer/Data/twitter_sexism_parsed_dataset.csv')
    df =df.astype(str).apply(lambda x: x.str.slice(0, 50))
    return df.to_html(max_rows=16,justify= 'left')

def d():
    
    df = pd.read_csv('/home/jules/Documentos/Personal/Sentiment_analyzer/Data/twitter_sexism_parsed_dataset.csv')
    return df.columns
    