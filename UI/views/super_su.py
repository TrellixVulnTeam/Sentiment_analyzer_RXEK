import streamlit as st 
import tkinter as tk 
from tkinter import filedialog
import os 
def serialized():
    

    # Set up tkinter
    root = tk.Tk()
    root.withdraw()

    # Make folder picker dialog appear on top of other windows
    root.wm_attributes('-topmost', 1)

    # Folder picker button
    st.title('Folder Picker')
    st.write('Please select a folder:')
    clicked = st.button('Folder Picker')

    st.write('write the file name :')
    file_name = st.text_input("").strip()
    if clicked:
        dirname = st.text_input('Selected folder:', filedialog.askdirectory(master=root))
        full_path = os.path.join(dirname,file_name)
        print(full_path)
        return full_path

def write():
    serialized()