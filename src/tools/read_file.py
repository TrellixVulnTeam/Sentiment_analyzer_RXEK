import marshal
def deserialize_file():
    fileIn = open("/home/jules/Documentos/Personal/TFG/Serialized/binary/Racism.dat", "br")
    dataLoad = marshal.load(fileIn)  
    fileIn.close()
    return dataLoad

