from sklearn import svm
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

data_processed = []
data_new = pd.DataFrame

for row in data.itertuples():
    stop_words = set(stopwords.words("english"))
    text = word_tokenize(row[3])

    text = [ps.stem(w) for w in text if not w in stop_words and w.isalnum()]
    text = ' '.join(text)
    data_processed.append(text)

data_new = data
data_new['Preprocessed_text'] = data_processed


##------------------------------------------------------------------##


badOfWordsModel = TfidfVectorizer()
badOfWordsModel.fit(data_new['Preprocessed_text'])
texts_BoW = badOfWordsModel.transform(data_new['Preprocessed_text'])

print(texts_BoW)


training_Data = data_new.head(4000)
print(training_Data)


svc = svm.SVC(kernel='linear')

X_train = texts_BoW
Y_train = training_Data['oh_label']

svc.fit(X_train, Y_train)
