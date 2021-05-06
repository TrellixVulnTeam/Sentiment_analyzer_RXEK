import pandas as pd


data = pd.read_csv('Data/pruebamulti.csv')

data_processed = []

for r in data.itertuples():
    text = r[4]
    cambio = r[5]
    if(text == "racism"):
        cambio=2
    data_processed.append(cambio)


data_nueva = data
data_nueva['oh_label'] = data_processed

df_shuffled=data_nueva.sample(frac=1).reset_index(drop=True)
df_shuffled.to_csv("Data/mix.csv",index=False)
