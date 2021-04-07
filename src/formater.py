
import pandas as pd
import csv
data = pd.read_csv('Data/twitter_sexism_parsed_dataset.csv')

def put_quot():
    for row in data.itertuples():
        res=row[3]
        if (res[0:1] != '"' or  res[0:3] == '"""'): 
            
            data['Text'] =  data['Text'].replace(res,'"'+res+'"')
        
    print(data.head(20))
    data.to_csv('Data/twitter_sexism_parsed_dataset_n.csv',engine='python')
put_quot()