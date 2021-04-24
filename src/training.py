import core 
import pandas as pd

from sklearn import svm
training_data = pd.read_csv('Data/twitter_sexism_parsed_dataset.csv')

#Se divide el Dataframe en 80-20
part_training = int(len(training_data)*0.8)
training_data = training_data.iloc[0:part_training]

#Tokenizamos y creamos la bolsa de palabras y los terminos de frecuencia del DataSet de entrenamiento
m_tokenization = core.make_tokenization(training_data)

BoWMethod = core.make_BoW(m_tokenization)

m_matrix = core.make_matrix(BoWMethod,m_tokenization)

#Definimos el tipo de kernel
svc = svm.SVC(kernel = "linear")

X_train = m_matrix
Y_train = training_data['oh_label']

#Entrenamos 
svc.fit(X_train,Y_train)
print ("ok")
#-----------------------------------------------------------#

test_data = pd.read_csv('Data/twitter_sexism_parsed_dataset.csv')
test_data = test_data.iloc[part_training:]


#Tokenizamos la parte de test, pero USAMOS LA MISMA BOW que en la parte de entrenamiento
m_tokenization_test = core.make_tokenization(test_data)
m_matrix_t = core.make_matrix(BoWMethod,m_tokenization_test)

X_test = m_matrix_t
predictions = svc.predict(X_test)

from sklearn.metrics import classification_report

Y_test = test_data['oh_label'] #Etiquetas reales de los documentos

print (classification_report(Y_test, predictions))
