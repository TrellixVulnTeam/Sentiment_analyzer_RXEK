
import streamlit as st
import os
from views import text_analysis
import pandas as pd
import tools.extra_functions
from annotated_text import annotated_text_file

def upload_file(folderpath='/home/jules/Documentos/Personal/Sentiment_analyzer/Data'):
    main_dict = {}
    st.title("Choose a file:")
    input_file = st.file_uploader("", type="csv")
    subir = st.button('Upload')

    if (subir == True and input_file is None):
        st.error("You must select a file ")
        subir = False
    elif (input_file is not None and subir == True):
        arch = os.path.join(folderpath, input_file.name)
        main_dict['path_upload_file'] = arch
        tools.extra_functions.dump("path_df.json",main_dict)
        return arch


def open_csv():
    csv_path = tools.extra_functions.load("path_df.json",'path_upload_file')

    if(csv_path is not None):
        df = pd.read_csv(csv_path)
        st.write(df)
        columns = df.columns
      
        option = st.selectbox('Choose a column to analyze', (columns))
        
        st.write('You selected:', option)
        lista = df[option].tolist()  
        num = st.select_slider("",range(len(lista)))
        st.write(num)
        for i in lista[0:num]:
            output_text(i)
        return lista
    else:
        st.warning("Dont data")
    

def output_text(input_text):

    word = input_text.split(' ')

    p = ['Cook', 'woman', 'shit']
    list_of_strings_ands_tuples = []

    for i in word:

        if(i in p):
            tuple1 = (i, "", "rgb(248, 239, 195)")
            list_of_strings_ands_tuples.append(tuple1)
        else:
            tuple2 = (i, "", "", "rgb(193, 193, 193)")

            list_of_strings_ands_tuples.append(tuple2)

    annotated_text_file(*list_of_strings_ands_tuples)
    print(list_of_strings_ands_tuples)


    
def write():
   
    upload_file()       
    open_csv()
    
    