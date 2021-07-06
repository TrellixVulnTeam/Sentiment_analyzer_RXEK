import nltk
from nltk import data
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer


nltk.download("stopwords")
nltk.download("punkt")


ps = PorterStemmer()
# Este metodo tokeniza el texto,se le pasa como parametro el DataFrame y retorna un nuevo DataFrame


# def make_tokenization(d):
#     d=pd.read_csv('/home/jules/Documentos/Personal/Sentiment_analyzer/tmp/twitter_sexism_parsed_dataset.csv')
#     data_processed = []
#     for row in d.itertuples():

#         stop_words = set(stopwords.words("english"))
#         text = word_tokenize(row[3])  # solucionar

#         text = [ps.stem(w)
#                 for w in text if not w in stop_words and w.isalnum()]

#         text = ' '.join(text)

#         data_processed.append(text)

#     data_new = d
#     data_new['Preprocessed_text'] = data_processed

#     return data_new

# # Este metodo crea la bolsa de palabras,recibiendo como parametro el DataFrame que retorna el metodo make_tokenization,
# # retorna la lista con todas las que contiene la BoW


# def make_BoW(dN):
#     bagOfWordsModel = TfidfVectorizer()
#     bagOfWordsModel.fit(dN['Preprocessed_text'])
#     return bagOfWordsModel


# # Este metodo crea la matriz con los terminos de frecuencia,recibiendo como parametro la BoW y la matriz que retorna make_tokenization


# def make_matrix(BoW_M, d):
#     texts_BoW = BoW_M.transform(d['Preprocessed_text'])
#     return texts_BoW

def make_tokenization(d):
    print('asdasdas',d)
    data_processed = []

    for row in d:
       for i in row:
            stop_words = set(stopwords.words("english"))
            text = word_tokenize(i)#solucionar

            text = [ps.stem(w)for w in text if not w in stop_words and w.isalnum()]
            # print(text)
            text = ' '.join(text)

            data_processed.append(text)
            # print('data',data_processed)

            return data_processed

# Este metodo crea la bolsa de palabras,recibiendo como parametro el DataFrame que retorna el metodo make_tokenization,
# retorna la lista con todas las que contiene la BoW


def make_BoW(dN):
    bagOfWordsModel = TfidfVectorizer()
    bagOfWordsModel.fit(dN)
    return bagOfWordsModel


# Este metodo crea la matriz con los terminos de frecuencia,recibiendo como parametro la BoW y la matriz que retorna make_tokenization


def make_matrix(BoW_M, d):
    texts_BoW = BoW_M.transform(d)
    return texts_BoW
