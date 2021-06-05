import streamlit as st
import os
import pandas as pd
import sys
sys.path.append('/home/jules/Documentos/Personal/TFG/src/tools')
import tools.extra_functions
sys.path.append('/home/jules/Documentos/Personal/TFG/UI/pages/views')
import underline_text



# settings output:
def div_size():
    f = open('/home/jules/Documentos/Personal/TFG/memory/size.txt', 'w')
    f.write('50')
    f.close()


def upload_file(folderpath='/home/jules/Documentos/Personal/TFG/Data'):
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
        columns = df.columns

        option_column = st.selectbox('Choose a column to analyze', (columns))

        st.write('You selected:', option_column)
        o = option()
        lista = df[option_column].tolist()
        num = st.sidebar.number_input("", step=1)
        st.write(num)
        for i in lista[0:num]:
            underline_text.output_text(o, i, "rgb(248, 239, 195)")
        return lista
    else:
        st.warning("Dont data")


def write():
    div_size()
    upload_file()
    open_csv()
