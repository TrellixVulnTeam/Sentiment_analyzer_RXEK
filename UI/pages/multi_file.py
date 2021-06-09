import streamlit as st
import os
import pandas as pd
import sys
sys.path.append('/home/jules/Documentos/Personal/Sentiment_analyzer/src/tools')
import tools.extra_functions
sys.path.append('/home/jules/Documentos/Personal/Sentiment_analyzer/UI/pages/views')
import underline_text
import plotly.graph_objects as go
import json
sys.path.append('/home/jules/Documentos/Personal/Sentiment_analyzer/src')
import training
# settings output:
def div_size():
    f = open('/home/jules/Documentos/Personal/Sentiment_analyzer/memory/size.txt', 'w')
    f.write('50')
    f.close()


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
        tools.extra_functions.dump("path_df.json", main_dict)
        return arch


def option():
    tipo = st.beta_columns(4)
    racismo = tipo[0].checkbox('Racism', key="r")
    machism = tipo[1].checkbox('Sexism', key="m")
    bullying = tipo[2].checkbox('Bullying', key="b")
    analysis = tipo[3].button(label="Analysis")

    if(racismo == True):
        return True


def open_csv():
    csv_path = tools.extra_functions.load("path_df.json", 'path_upload_file')

    if(csv_path is not None):
        df = pd.read_csv(csv_path)
        st.write(df)       

        option_column = st.selectbox('Choose a column to analyze', (df.columns))
        
        st.write('You selected:', option_column)
        
        o = option()
        lista = df[option_column].tolist()
        num = st.sidebar.number_input("", step=1)
        m =[]
        for i in lista[0:num]:
            underline_text.output_text(o, i, "rgb(248, 239, 195)")
            m.append(training.classifier(i))
        with open("/home/jules/Documentos/Personal/Sentiment_analyzer/R.txt", 'a') as filehandle:
                    json.dump(m, filehandle)    
        return lista
    else:
        st.warning("Dont data")
def clear_data():
    open('/home/jules/Documentos/Personal/Sentiment_analyzer/R.txt', 'w').close
    
def chart():
    with open('/home/jules/Documentos/Personal/Sentiment_analyzer/R.txt', 'r') as filehandle:
        if os.stat('/home/jules/Documentos/Personal/Sentiment_analyzer/R.txt').st_size != 0:
            s = json.load(filehandle)
            listaa = []
            
            a=0
            for i in s:
                a+=i
            a=a/len(s) 
            nr=1-a
            listaa.append(nr)
            listaa.append(a)

            print(a)

            labels = ['No racism','Racism']            
            st.markdown("### Chart analysis")
            fig = go.Figure(data=[go.Pie(labels=labels, values=listaa)])
            st.write(fig)
def write():
    clear_data()
    div_size()
    upload_file()
    open_csv()
    chart()