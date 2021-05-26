import core
import pandas as pd
from sklearn.metrics import classification_report
from sklearn import svm
from sklearn.calibration import CalibratedClassifierCV
training_data = pd.read_csv('Data/twitter_sexism_parsed_dataset.csv')

# Se divide el Dataframe en 80-20
part_training = int(len(training_data)*0.8)
training_data = training_data.iloc[0:part_training]
print(training_data.shape)
# Tokenizamos y creamos la bolsa de palabras y los terminos de frecuencia del DataSet de entrenamiento
m_tokenization = core.make_tokenization(training_data)

BoWMethod = core.make_BoW(m_tokenization)

m_matrix = core.make_matrix(BoWMethod, m_tokenization)

# Definimos el tipo de kernel
svc = svm.SVC()
print("OKlll")
clf = CalibratedClassifierCV(svc)


X_train = m_matrix
Y_train = training_data['oh_label']

# Entrenamos
clf.fit(X_train, Y_train)

print("ok")
#-----------------------------------------------------------#

test_data = pd.read_csv('Data/twitter_sexism_parsed_dataset.csv')
test_data = test_data.iloc[part_training:]

print('testDATA', test_data.shape)

# Tokenizamos la parte de test, pero USAMOS LA MISMA BOW que en la parte de entrenamiento
m_tokenization_test = core.make_tokenization(test_data)
m_matrix_t = core.make_matrix(BoWMethod, m_tokenization_test)

X_test = m_matrix_t
y_proba = clf.predict_proba(X_test)


Y_test = test_data['oh_label']  # Etiquetas reales de los documentos

counter = 1
for i in y_proba:

    print(i*100, '---', counter)
    counter += 1
