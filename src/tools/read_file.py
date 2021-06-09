import marshal
def deserialize_file():
    fileIn = open("/home/jules/Documentos/Personal/Sentiment_analyzer/Serialized/binary/Racism.dat", "br")
    dataLoad = marshal.load(fileIn)  
    fileIn.close()
    return dataLoad

