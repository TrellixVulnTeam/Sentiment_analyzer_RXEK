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
data_processed = []

def make_tokenization():
    for row in data.itertuples():
        stop_words = set(stopwords.words("english"))
        text = word_tokenize(row[3])

        text = [ps.stem(w) for w in text if not w in stop_words and w.isalnum()]
        text = ' '.join(text)
        data_processed.append(text)

    data_new = data
    data_new['Preprocessed_text'] = data_processed
 
    return data_new


##------------------------------------------------------------------##

def BoW(d):
    Bag_of_Words=TfidfVectorizer()
    Bag_of_Words.fit(data['Preprocessed_text'])
    text_vectoricer = Bag_of_Words.transform(data['Preprocessed_text'])
    print(text_vectoricer)
   

mt = make_tokenization()
BoW(mt)