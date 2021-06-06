import core
import pandas as pd
from sklearn.metrics import classification_report
from sklearn import svm
from sklearn.calibration import CalibratedClassifierCV
import marshal
import joblib

# def create_File(BoW):
#     path_file = '/home/jules/Documentos/Personal/TFG/Serialized/Racism.dat'
#     fileOut = open(path_file, "bw")
#     marshal.dump(BoW, fileOut)
#     fileOut.close()


# training_data = pd.read_csv('/home/jules/Documentos/Personal/TFG/Data/twitter_racism_parsed_dataset.csv')

# # Se divide el Dataframe en 80-20
# part_training = int(len(training_data)*0.8)
# training_data = training_data.iloc[0:part_training]

# # Tokenizamos y creamos la bolsa de palabras y los terminos de frecuencia del DataSet de entrenamiento
# m_tokenization = core.make_tokenization(training_data)
# BoWMethod = core.make_BoW(m_tokenization)
# joblib.dump(BoWMethod,'BoW.pkl')

# m_matrix = core.make_matrix(BoWMethod, m_tokenization)

# # Definimos el tipo de kernel
# svc = svm.SVC()
# # saved = joblib.dump(svc,'fielname.pkl')

# clf = CalibratedClassifierCV(svc)
# joblib.dump(clf,'clf.pkl')
# X_train = m_matrix
# Y_train = training_data['oh_label']

# # Entrenamos

# clf.fit(X_train, Y_train)
# # BoW_names = BoWMethod.get_feature_names()
# # create_File(BoW_names)



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



    
test_data = pd.read_csv('Data/twitter_sexism_parsed_dataset.csv')
test_data = test_data.iloc[10778:]

print('testDATA', test_data.shape)

# Tokenizamos la parte de test, pero USAMOS LA MISMA BOW que en la parte de entrenamiento
m_tokenization_test = core.make_tokenization(test_data)
BoWMethod = joblib.load('BoW.pkl') 
m_matrix_t = core.make_matrix(BoWMethod, m_tokenization_test)

X_test = m_matrix_t

clf = joblib.load('clf.pkl') 

a = clf.predict(X_test)
print(a)