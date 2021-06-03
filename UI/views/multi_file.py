import streamlit as st
import os
from views import text_analysis
import pandas as pd
import tools.extra_functions


def upload_file(folderpath='/home/jules/Documentos/Personal/TFG/Data'):
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
        print(type(columns))
        option = st.selectbox('Choose a column to analyze', (columns))
        
        st.write('You selected:', option)
        lista = df[option].tolist()
        for i in lista[0:9]:
            text_analysis.output_text(i)
    else:
        st.warning("Dont data")



def write():
    upload_file()        
    open_csv()
    
    