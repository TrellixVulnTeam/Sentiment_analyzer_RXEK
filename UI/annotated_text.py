import marshal
import pandas as pd


def procesed_text(text, c):

    if(text != ''):
        key_words = deserialize_file()
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
        key_words = deserialize_file()
        if(c == ''):
            color = 'black'
        else:
            color = str(c)
        df = pd.read_csv(path)
        lista = []
        print(f)
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
        return df.to_html(max_rows=16, justify='left', index=False)


def d(arc):
    lista= []
    if(arc != ''):
        df = pd.read_csv(arc)
        for i in df.columns:
            lista.append(i)
        return lista
