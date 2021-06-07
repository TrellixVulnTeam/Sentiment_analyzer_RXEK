import core
import pandas as pd
from sklearn.metrics import classification_report
from sklearn import svm
from sklearn.calibration import CalibratedClassifierCV
import marshal
import joblib
import streamlit as st
def create_File(BoW):
    path_file = '/home/jules/Documentos/Personal/TFG/Serialized/binary/Racism.dat'
    fileOut = open(path_file, "bw")
    marshal.dump(BoW, fileOut)
    fileOut.close()




def training_part():
    # Tokenizamos y creamos la bolsa de palabras y los terminos de frecuencia del DataSet de entrenamiento
    training_data = pd.read_csv('/home/jules/Documentos/Personal/TFG/Data/twitter_racism_parsed_dataset.csv')

# Se divide el Dataframe en 80-20
    part_training = int(len(training_data)*0.8)
    training_data = training_data.iloc[0:part_training]

    m_tokenization = core.make_tokenization(training_data)
    BoWMethod = core.make_BoW(m_tokenization)

    joblib.dump(BoWMethod, '/home/jules/Documentos/Personal/TFG/Serialized/plk/BoW/BoW_Racism.pkl')

    m_matrix = core.make_matrix(BoWMethod, m_tokenization)

    # Definimos el tipo de kernel
    svc = svm.SVC(probability=True)
    

    clf = CalibratedClassifierCV(svc)
    joblib.dump(clf, 'clf.pkl')
    X_train = m_matrix
    Y_train = training_data['oh_label']

    # Entrenamos

    clf.fit(X_train, Y_train)
    classifier = clf.fit(X_train, Y_train)
    joblib.dump(classifier, '/home/jules/Documentos/Personal/TFG/Serialized/plk/classifiers/racism_clf_.pkl')
    BoW_names = BoWMethod.get_feature_names()
    create_File(BoW_names)

# training_part()
#-----------------------------------------------------------#

def classifier(text):
    v=[]
    # text = "ISIS beheads people. Saudi beheads people. Mohammed beheaded 600 Jews"
   
    v.append(text)
    print(v)

    # Tokenizamos la parte de test, pero USAMOS LA MISMA BOW que en la parte de entrenamiento
    m_tokenization_test = core.make_tokenization(v)
    BoWMethod = joblib.load('/home/jules/Documentos/Personal/TFG/Serialized/plk/BoW/BoW_Racism.pkl') 

    m_matrix_t = core.make_matrix(BoWMethod, m_tokenization_test)

    X_test = m_matrix_t
    
    clf = joblib.load('/home/jules/Documentos/Personal/TFG/Serialized/plk/classifiers/racism_clf_.pkl') 

    cla = clf.predict_proba(X_test)
    return cla
   

# def test_part_algortihm():

#     (BoWMethod,clf) = training_part_algorithm(DF,num)
#     test_data = pd.read_csv('Data/twitter_sexism_parsed_dataset.csv')
#     test_data = test_data.iloc[part_training:]

#     print('testDATA', test_data.shape)

#     # Tokenizamos la parte de test, pero USAMOS LA MISMA BOW que en la parte de entrenamiento
#     m_tokenization_test = core.make_tokenization(test_data)
#     m_matrix_t = core.make_matrix(BoWMethod, m_tokenization_test)

#     X_test = m_matrix_t
#     y_proba = clf.predict_proba(X_test)


#     Y_test = test_data['oh_label']  # Etiquetas reales de los documentos

#     print(y_proba)


# test_data = pd.read_csv('Data/twitter_sexism_parsed_dataset.csv')
# test_data = test_data.iloc[10778:]

# print('testDATA', test_data.shape)

# # Tokenizamos la parte de test, pero USAMOS LA MISMA BOW que en la parte de entrenamiento
# m_tokenization_test = core.make_tokenization(test_data)
# BoWMethod = joblib.load('filename.pkl')
# m_matrix_t = core.make_matrix(BoWMethod, m_tokenization_test)

# X_test = m_matrix_t

# clf = joblib.load('clf.pkl')

# a = clf.predict(X_test)
# print(a)
