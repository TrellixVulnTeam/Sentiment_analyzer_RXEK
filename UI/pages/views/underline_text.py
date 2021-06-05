from annotated_text import annotated_text   
import sys

sys.path.append('/home/jules/Documentos/Personal/TFG/src/tools')
import read_file
def output_text(flag,input_text,color_p):
   
    print(flag)
    word = input_text.split(' ')
    text_color(flag,word,color_p)

def text_color(flag,lista,color_p):
    p = read_file.deserialize_file()
    color_p = str(color_p)
    if(flag == True):
        
        list_of_strings_ands_tuples = []

        for i in lista:

            if(i in p):
                tuple1 = (i, "", color_p)
                list_of_strings_ands_tuples.append(tuple1)
            else:
                tuple2 = (i, "", "", "rgb(193, 193, 193)")

                list_of_strings_ands_tuples.append(tuple2)

        annotated_text(*list_of_strings_ands_tuples)

    else:
               
        list_of_strings_ands_tuples = []

        for i in lista:

            if(i in p):
                tuple1 = (i, "", "")
                list_of_strings_ands_tuples.append(tuple1)
            else:
                tuple2 = (i, "", "", "")

                list_of_strings_ands_tuples.append(tuple2)

        annotated_text(*list_of_strings_ands_tuples)
        print(list_of_strings_ands_tuples)
