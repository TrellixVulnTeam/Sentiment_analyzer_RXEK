import json

import marshal
import streamlit as st
import tkinter as tk
from tkinter import filedialog
import os
import sys
sys.path.append('../src')

import training
import tools.extra_functions 


def entrenamiento(folderpath='/home/jules/Documentos/Personal/Sentiment_analyzer/Data'):

    serialized()
    st.markdown("## Select the training part of the DataFrame")
    training_part = st.select_slider("", options=range(101))/100

    st.markdown("## Select the CSV File")

    input_file = st.file_uploader("", type="csv")
    subir = st.button('Upload')

    

    if (subir == True and input_file is None):
        st.error("You must select a file ")
        subir = False
    elif (input_file is not None and subir == True):
        arch = os.path.join(folderpath, input_file.name)

        training.training_part_algorithm(arch, training_part)


def serialized():
    main_dict = {}
    # Set up tkinter
    root = tk.Tk()
    root.withdraw()

    # Make folder picker dialog appear on top of other windows
    root.wm_attributes('-topmost', 1)

    st.title('Write the file name :')
    file_name = str(st.text_input(""))
    file_name = file_name.replace(' ', '_')
    # Folder picker button
    st.title('Folder Picker')

    clicked = st.button('Folder Picker')

    if (clicked and file_name is not None):
        dirname = filedialog.askdirectory(master=root)
        full_path = st.text_input( 'Selected folder:', os.path.join(dirname, file_name))
        main_dict['full_path'] = full_path
        tools.extra_functions.dump(main_dict)

        return full_path
  


def write():
    
    entrenamiento()
