import streamlit as st
import pandas as pd
import os
import sys
# import matplotlib.pyplot as plt
import numpy as np

sys.path.append('../src')

import pages.text_analysis
import pages.multi_file



PAGES = {
    "Text Analysis": pages.text_analysis,
    "Multi File": pages.multi_file,
    
}


def sidebar():
   
   selection = st.sidebar.radio("",list(PAGES.keys()))
   page = PAGES[selection]
   page.write()
# ----------------------------------------------------------------------------------


def main():
    sidebar()
  


if __name__ == '__main__':
    main()
