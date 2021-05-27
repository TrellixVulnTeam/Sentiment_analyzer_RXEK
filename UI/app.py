import core
import streamlit as st
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.append('../src')

# Methods


def upload_file(folderpath='/home/jules/Documentos/Personal/Sentiment_analyzer/Data'):
    st.title("First Choose a file:")
    input_file = st.file_uploader("", type="csv")
    subir = st.button('Upload')

    if (subir == True and input_file is None):
        st.error("You must select a file ")
        subir = False
    elif (input_file is not None and subir == True):
        arch = os.path.join(folderpath, input_file.name)
        return arch


def type_text():
    st.title("Or type a text to analyze:")
    texto = st.text_input(label="", value="Type a text")

    if(len(texto) == 0):
        st.error("The text cannot be empty  ")
    return texto


def make(archivo):
    df = pd.read_csv(archivo)

    with st.spinner('Proccesing data, wait for it...'):
        bar = st.progress(0)

        tokenizacion = core.make_tokenization(df)
        bar.progress(20)

        BoWM = core.make_BoW(tokenizacion)
        bar.progress(40)

        matrix = core.make_matrix(BoWM, tokenizacion)
        bar.progress(100)

    st.success('Done!')


def make_graph():
    st.markdown("# Analysis results:")
    chart_data = pd.DataFrame(np.random.randn(50, 3), columns=[
                              "Sexism", "Bullyng", "Racism"])
    st.bar_chart(chart_data)

# ----------------------------------------------------------------------------------


def main():

    file_path = upload_file()
    type_text()

    if(file_path is not None):

        make(file_path)
        make_graph()


if __name__ == '__main__':
    main()
