import os.path
def check(file):
    return os.path.isfile(file)
def load(file):
    data = []
    try:
        fo = open(file, "r")
        data = fo.readlines()
        fo.close()
        sdata = []
        for p in data:
            sdata.append(p.strip("\n"))
        return sdata
    except:
        print("load error")
def append(data, file):
    try:
        fo = open(file, "a")
        fo.write(str(data)+"\n")
        fo.close()
    except:
        print("append error")
def newFile(file):
    try:
        fo = open(file, "w")
        fo.close()
    except:
        print("newfile error")
