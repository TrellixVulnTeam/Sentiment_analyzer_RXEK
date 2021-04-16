import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download("stopwords")
nltk.download("punkt")

data = pd.read_csv('Data/twitter_sexism_parsed_dataset.csv')
ps = PorterStemmer()

mt = pd.DataFrame()
data_processed = BoW_Modelo = txtBoW = []


def make_tokenization():
    for row in data.itertuples():
        stop_words = set(stopwords.words("english"))
        text = word_tokenize(row[3])

        text = [ps.stem(w)
                        for w in text if not w in stop_words and w.isalnum()]
        text = ' '.join(text)
        data_processed.append(text)

    data_new = data
    data_new['Preprocessed_text'] = data_processed

    return data_new


##------------------------------------------------------------------##

def make_BoW(d):
    bagOfWordsModel = TfidfVectorizer()
    bagOfWordsModel.fit(d['Preprocessed_text'])
    return bagOfWordsModel

def make_matrix(BoW_M,d):
    texts_BoW = BoW_M.transform(d['Preprocessed_text'])
    print(texts_BoW)
    return texts_BoW
    

mt=make_tokenization()
BoW_Modelo = make_BoW(mt)
make_matrix(BoW_Modelo,mt)