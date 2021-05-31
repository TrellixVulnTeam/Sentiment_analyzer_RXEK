import streamlit as st
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.append('../src')
import core
# Methods


import views.text_analysis
import views.multi_file


PAGES = {
    "Text Analysis": views.text_analysis,
    "Multi File": views.multi_file
}


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


def sidebar():
   st.sidebar.title("Choose a option")
   selection = st.sidebar.radio("",list(PAGES.keys()))
   page = PAGES[selection]
   page.write()
# ----------------------------------------------------------------------------------


def main():
    sidebar()
  


if __name__ == '__main__':
    main()
