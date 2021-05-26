
import streamlit as st
import pandas as pd
import os
import sys


sys.path.append('../src')

import core

#Methods
def upload_file(folderpath ='/home/jules/Documentos/Personal/TFG/Data'):

    input_file = st.file_uploader("", type="csv")
    subir = st.button('Upload')   

    if (subir == True and input_file is None):
        st.error("Debe seleccionar un archivo")
        subir = False
    elif (input_file is not None and subir == True):
        arch= os.path.join(folderpath,input_file.name)
        return arch
           

        

def make(archivo):
    df=pd.read_csv(archivo)

    bar = st.progress(0)
    
    tokenizacion = core.make_tokenization(df)
    bar.progress(20)

    BoWM = core.make_BoW(tokenizacion)
    bar.progress(40)

    matrix = core.make_matrix(BoWM, tokenizacion)
    bar.progress(100)
    
        
#----------------------------------------------------------------------------------

def main():
 
 st.title("First Choose a file:")
 file_path = upload_file()

 if(file_path is not None):
    st.title("Now take button Analysis:") 

    make(file_path)
   
 
if __name__ == '__main__':
 main()

