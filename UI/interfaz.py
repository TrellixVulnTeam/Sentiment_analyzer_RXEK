import streamlit as st
import pandas as pd
import os

arr = ["page1"]
add_selec = st.sidebar.selectbox("kaka",arr)

def upload_file():

    input_file = st.file_uploader("", type="csv")
    subir = st.button('Upload')
    if (input_file is not None and subir == True):

        arr.append("new page")
        add_selec = st.sidebar.selectbox("kaka",arr)
        df = pd.read_csv(input_file)
        st.write(df.head(100))

    elif (subir == True and input_file is None):
        st.error("Debe seleccionar un archivo")
        subir = False


upload_file()
