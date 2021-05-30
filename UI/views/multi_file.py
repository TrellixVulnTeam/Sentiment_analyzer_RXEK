import streamlit as st
import os 
from views import text_analysis

def upload_file(folderpath='/home/jules/Documentos/Personal/TFG/Data'):
    st.title("Choose a file:")
    input_file = st.file_uploader("", type="csv")
    subir = st.button('Upload')

    if (subir == True and input_file is None):
        st.error("You must select a file ")
        subir = False
    elif (input_file is not None and subir == True):
        arch = os.path.join(folderpath, input_file.name)
        return arch
def a ():
    return "a"
def output_text(input_text):
    st.title("Output text")
    texto_salida = st.text_area(label="", value=input_text,key="output",height = 250)    
    return texto_salida


def write():
    upload_file()
    text_analysis.option()
    text_analysis.output_text(a())