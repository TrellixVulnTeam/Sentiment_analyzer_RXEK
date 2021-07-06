import marshal
from os import path
from zipfile import Path
from flask import json
import pandas as pd
import sys
sys.path.append('/home/jules/Documentos/Personal/Sentiment_analyzer/src/')
import training as t

def procesed_text(text, c):

    if(text != ''):
        key_words = deserialize_file(c)
        color = str(c)
        text = text.split(' ')
        lista = []
        for i in text:
            if(i in key_words):
                t = '<span class='+color+'>' + i + '</span>'
                lista.append(t)
            else:
                t = '<span class="no-color" >' + i + '</span>'
                lista.append(t)
        strA = " ".join(lista)
        return strA

def procesed_csv(path, c, f):

    if(path != ''):
        key_words = deserialize_file(c)

        if(c == ''):
            color = 'black'
        else: 
            color = str(c)
        df = pd.read_csv(path)
        
        l=[]
        for row in df[f][0:100]:
            lista = []
            text = row.split(' ')

            for i in text:
                if(i in key_words):
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
def texto_documento(path,f,clasifier,bow):
    
    if(path != ''):  
      
        df = pd.read_csv(path)
        lista = []
        p=[]
        for row in df[f][0:10]:
          
           lista.append(row)
           p.append(t.classifier(row,clasifier,bow))
       
        data={"text":lista,"porcentaje":p}
        
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
        return df.to_html(max_rows=16, justify='left', index=False)

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
    f=open (path,'r')
    data = f.read()
    data=data.replace('"','')
    return data