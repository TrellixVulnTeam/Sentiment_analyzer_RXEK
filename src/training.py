import core
import pandas as pd
from sklearn.metrics import classification_report
from sklearn import svm
from sklearn.calibration import CalibratedClassifierCV
import marshal
import json
import tools.extra_functions

def create_File(response):
    path_file = '/home/jules/Documentos/Personal/TFG/Serialized/sexism.'
    fileOut = open(path_file, "bw")
    marshal.dump(response, fileOut)
    fileOut.close()

def training_part_algorithm(DF,num):
    training_data = pd.read_csv(DF)
    print(num)
    # Se divide el Dataframe en 80-20
    part_training = int(len(training_data)*num)
    training_data = training_data.iloc[0:part_training]

    # Tokenizamos y creamos la bolsa de palabras y los terminos de frecuencia del DataSet de entrenamiento
    m_tokenization = core.make_tokenization(training_data)
    BoWMethod = core.make_BoW(m_tokenization)
    m_matrix = core.make_matrix(BoWMethod, m_tokenization)

    # Definimos el tipo de kernel
    svc = svm.SVC()
    clf = CalibratedClassifierCV(svc)
    X_train = m_matrix
    Y_train = training_data['oh_label']

    # Entrenamos

    clf.fit(X_train, Y_train)
    BoW_names = BoWMethod.get_feature_names()
    create_File(BoW_names)
    return BoWMethod


#-----------------------------------------------------------#


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
