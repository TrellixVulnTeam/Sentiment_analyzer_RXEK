import streamlit as st
from annotated_text import annotated_text
# styles


# --------------------------------------------
def type_itext():

    st.title("Type a text to analyze:")
    __, __, __, __, __, __, __, col_button = st.beta_columns(8)
    with col_button:
        enviar = st.button('Send')
    texto_entrada = st.text_area(label="", value="", key="input", height=250)

    return texto_entrada


def option():

    tipo = st.beta_columns(4)
    racismo = tipo[0].checkbox('Racism', key="r")
    machism = tipo[1].checkbox('Sexism', key="m")
    bullying = tipo[2].checkbox('Bullying', key="b")
    analysis = tipo[3].button(label="Analysis")


def output_text(input_text):

    word = input_text.split(' ')

    p = ['Cook', 'woman', 'shit']
    list_of_strings_ands_tuples = []

    for i in word:

        if(i in p):
            tuple1 = (i, "", "rgb(248, 239, 195)")
            list_of_strings_ands_tuples.append(tuple1)
        else:
            tuple2 = (i, "", "", "rgb(193, 193, 193)")

            list_of_strings_ands_tuples.append(tuple2)

    annotated_text(*list_of_strings_ands_tuples)
    print(list_of_strings_ands_tuples)


def clear_data():
    open('/home/jules/Documentos/Personal/Sentiment_analyzer/memory/path_df.json', 'w').close


def write():

    clear_data()
    input_t = type_itext()
    option()
    output_text(input_t)
