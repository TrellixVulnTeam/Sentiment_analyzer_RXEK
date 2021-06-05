import json
import os
def dump(name,dict):
    path_dir = '/home/jules/Documentos/Personal/TFG/memory'
    full_path = os.path.join(path_dir,name)

    with open(full_path, 'w') as fp:
        json.dump(dict, fp)

def load(name,index_name):
    path_dir = '/home/jules/Documentos/Personal/TFG/memory'
    full_path = os.path.join(path_dir,name)
    if os.stat(full_path).st_size != 0:
        
        with open(full_path) as json_file:
            data = json.load(json_file)
            print(data)
            path_f=str(data[index_name])
            return path_f


