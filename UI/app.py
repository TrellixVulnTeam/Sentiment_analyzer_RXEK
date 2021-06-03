import streamlit as st
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.append('../src')
import core

import views.text_analysis
import views.multi_file



PAGES = {
    "Text Analysis": views.text_analysis,
    "Multi File": views.multi_file,
    
}


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
