import streamlit as st
import sys
import json
sys.path.append('/home/jules/Documentos/Personal/TFG/src/tools')

sys.path.append('/home/jules/Documentos/Personal/TFG/UI/pages/views')
import underline_text
sys.path.append('/home/jules/Documentos/Personal/TFG/src')
import training
import plotly.express as px
# styles
def div_size():
    f = open('/home/jules/Documentos/Personal/TFG/memory/size.txt','w')
    f.write('400')
    f.close()
# --------------------------------------------
def type_itext():
    
    st.title("Type a text to analyze:")
    __, __, __, __, __, __, __, col_button = st.beta_columns(8)
    with col_button:
        enviar = st.button('Send')
        print(enviar)
    texto_entrada = st.text_area(label="", value="", key="input", height=250)
    if(enviar == True and texto_entrada is not None ):
        
        s = training.classifier(texto_entrada)
      
        st.markdown(s)
        enviar= True
    return texto_entrada


def option():

    tipo = st.beta_columns(4)
    racismo = tipo[0].checkbox('Racism', key="r")
    machism = tipo[1].checkbox('Sexism', key="m")
    bullying = tipo[2].checkbox('Bullying', key="b")
    analysis = tipo[3].button(label="Analysis")
   
    if(racismo == True):
        
        return True

def chart():
    with open('/home/jules/Documentos/Personal/TFG/R.txt', 'r') as filehandle:
        s = json.load(filehandle)
        fig = px.pie( values=s)
        st.write(fig)

def clear_data():
    open('/home/jules/Documentos/Personal/TFG/memory/path_df.json', 'w').close


def write():
    
    clear_data()
    div_size()
    input_t = type_itext()
        
    underline_text.output_text(option(),input_t,"rgb(248, 239, 195)")
    chart()
  
