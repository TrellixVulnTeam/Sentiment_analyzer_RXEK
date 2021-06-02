import streamlit as st
import os
from views import text_analysis
import pandas as pd
import tools.extra_functions


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
        tools.extra_functions.dump(main_dict)
        return arch


def open_csv():
    csv_path = tools.extra_functions.load('path_upload_file')

    if(csv_path is not None):
        df = pd.read_csv(csv_path)
        st.write(df)
        columns = df.columns
        option = st.selectbox('How would you like to be contacted?', (columns))
        st.write('You selected:', option)
    else:
        st.warning("Dont data")


def write():
    upload_file()
    open_csv()
    text_analysis.option()
