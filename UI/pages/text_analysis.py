import streamlit as st
import sys
import json
sys.path.append('/home/jules/Documentos/Personal/Sentiment_analyzer/src/tools')

sys.path.append('/home/jules/Documentos/Personal/Sentiment_analyzer/UI/pages/views')
import underline_text
sys.path.append('/home/jules/Documentos/Personal/Sentiment_analyzer/src')
import training
import plotly.graph_objects as go
import os
# styles
def div_size():
    f = open('/home/jules/Documentos/Personal/Sentiment_analyzer/memory/size.txt','w')
    f.write('200')
    f.close()
# --------------------------------------------
def type_itext():
    
    st.title("Type a text to analyze:")
    __, __, __, __, __, __, col_button = st.beta_columns(7)
    with __,col_button:
        enviar = st.button('Send & Analysis')
       
    
    texto_entrada = st.text_area(label="", value="", key="input", height=250)
    if(enviar == True and texto_entrada is not None ):        
        training.classifier(texto_entrada)    
      
    return texto_entrada


def option():

    tipo = st.beta_columns(3)
    racismo = tipo[0].checkbox('Racism', key="r")
    machism = tipo[1].checkbox('Sexism', key="m")
    bullying = tipo[2].checkbox('Bullying', key="b")
    
   
    if(racismo == True):
        
        return racismo
   

def chart():
    with open('/home/jules/Documentos/Personal/Sentiment_analyzer/R.txt', 'r') as filehandle:
        if os.stat('/home/jules/Documentos/Personal/Sentiment_analyzer/R.txt').st_size != 0:
            s = json.load(filehandle)
            labels = ['No racism','Racism']            
            st.markdown("### Chart analysis")
            fig = go.Figure(data=[go.Pie(labels=labels, values=s)])
            st.write(fig)
    # open('/home/jules/Documentos/Personal/Sentiment_analyzer/R.txt', 'w').close


def clear_data():
    open('/home/jules/Documentos/Personal/Sentiment_analyzer/memory/path_df.json', 'w').close
    
def write():
    
    clear_data()
    div_size()
    input_t = type_itext()
        
    underline_text.output_text(option(),input_t,"rgb(248, 239, 195)")
    chart()
  
