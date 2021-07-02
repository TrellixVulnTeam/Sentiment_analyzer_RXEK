import marshal
from os import path
import pandas as pd


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
        lista = []

        for row in df[f][0:100]:

            text = row.split(' ')

            for i in text:
                if(i in key_words):
                    t = '<span class='+color+'>' + i + '</span>'
                    lista.append(t)
                else:
                    t = '<span class="no-color" >' + i + '</span>'
                    lista.append(t)
            lista.append('</br>')

        strA = " ".join(lista)
        return strA

def texto_documento(path,f):

    if(path != ''):  
      
        df = pd.read_csv(path)
        lista = []
        
        for row in df[f][0:10]:
            
            text = row.split(' ')            
            for i in text:
                lista.append(i)
        
        strA = " ".join(lista)
        return strA

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
    print(BoW)
    return BoW

def select_clf(key):

    if(key == 'racism'):
        clf = "/home/jules/Documentos/Personal/Sentiment_analyzer/Serialized/plk/classifiers/racism_clf_.pkl"
    elif(key == 'sexism'):
        clf = "/home/jules/Documentos/Personal/Sentiment_analyzer/Serialized/plk/classifiers/sexism_clf_.pkl"
    print(clf)
    return clf

def select_BoW_pkl(key):

    if(key == 'racism'):
        BoW = "/home/jules/Documentos/Personal/Sentiment_analyzer/Serialized/plk/BoW/BoW_Racism.pkl"
    elif(key == 'sexism'):
        BoW = "/home/jules/Documentos/Personal/Sentiment_analyzer/Serialized/plk/BoW/BoW_Sexism.pkl"
    print(BoW)
    return BoW