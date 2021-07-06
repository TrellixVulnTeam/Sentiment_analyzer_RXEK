import core_string
import pandas as pd
from sklearn.metrics import classification_report
from sklearn import svm
from sklearn.calibration import CalibratedClassifierCV
import marshal
import joblib

import json 
def create_File(BoW):
    path_file = '/home/jules/Documentos/Personal/Sentiment_analyzer/Serialized/binary/Sexism.dat'
    fileOut = open(path_file, "bw")
    marshal.dump(BoW, fileOut)
    fileOut.close()




def training_part():
    # Tokenizamos y creamos la bolsa de palabras y los terminos de frecuencia del DataSet de entrenamiento
    training_data = pd.read_csv('/home/jules/Documentos/Personal/Sentiment_analyzer/Data/twitter_sexism_parsed_dataset.csv')

# Se divide el Dataframe en 80-20
    part_training = int(len(training_data)*0.8)
    training_data = training_data.iloc[0:part_training]

    m_tokenization = core_string.make_tokenization(training_data)
    BoWMethod = core_string.make_BoW(m_tokenization)

    joblib.dump(BoWMethod, '/home/jules/Documentos/Personal/Sentiment_analyzer/Serialized/plk/BoW/BoW_Sexism.pkl')

    m_matrix = core_string.make_matrix(BoWMethod, m_tokenization)

    # Definimos el tipo de kernel
    svc = svm.SVC(probability=True)
    

    clf = CalibratedClassifierCV(svc)    
    X_train = m_matrix
    Y_train = training_data['oh_label']

    # Entrenamos

    clf.fit(X_train, Y_train)
    classifier = clf.fit(X_train, Y_train)
    joblib.dump(classifier, '/home/jules/Documentos/Personal/Sentiment_analyzer/Serialized/plk/classifiers/sexism_clf_.pkl')
    BoW_names = BoWMethod.get_feature_names()
    create_File(BoW_names)

# training_part()
#-----------------------------------------------------------#

def classifier(text,clasifier,bow):
    
    text=text.split(',')
    v=[] 

  
    v.append(text)   
   
    # Tokenizamos la parte de test, pero USAMOS LA MISMA BOW que en la parte de entrenamiento
    m_tokenization_test = core_string.make_tokenization(v)
    BoWMethod = joblib.load(bow) 

    m_matrix_t = core_string.make_matrix(BoWMethod, m_tokenization_test)

    X_test = m_matrix_t
    
    clf = joblib.load(clasifier) 
    l=[]
    cla = clf.predict_proba(X_test)
    calculo=1-(cla[0][1])
    l.append(calculo)
    l.append(cla[0][1])
   
    return l
    # for i in cla:
        
    #     l.append(i)
    # print(l)
    # strA=','.join(l)
    # return strA
    
        
        
    
        
 