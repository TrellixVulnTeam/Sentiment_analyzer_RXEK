import marshal
def deserialize_file():
    fileIn = open("/home/jules/Documentos/Personal/TFG/Serialized/Sexism.dat", "br")
    dataLoad = marshal.load(fileIn)  
    fileIn.close()
    return dataLoad

