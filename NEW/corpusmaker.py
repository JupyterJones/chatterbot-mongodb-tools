import json
import os  
import string
import io

from ruamel.yaml import YAML
from ruamel.yaml.reader import Reader

yaml = YAML(typ='safe')


def strip_invalid(s):
    res = ''
    for x in s:
        if Reader.NON_PRINTABLE.match(x):
            # res += '\\x{:x}'.format(ord(x))
            continue
        res += x
    return res


def convert(filename) :
    count = 0
    #ALL = [] 
    
    #f = io.open(filename, mode="r", encode("latin_1"),decode("utf_8")).readlines()
    f = io.open(filename, mode="r", encoding="utf-8").readlines()
    #f = open(filename, "r").readlines()
    for line in f:
        line = line.encode('utf8').decode('latin1')
        line = line.replace("\n","")
        line =line.replace("\"","'")
        line=line.replace("\\","")
        line=line.replace("{","")
        line=line.replace("}","")
        line = strip_invalid(line)
        count=count+1
        newline =[]
        txt = "[\""
        if(count % 2 != 0):
            newline.append(""+line +"")
            txt2 = txt+line
        if(count % 2 == 0):
            newline.append(""+line +"")
            txt3 = txt2 +"\",\n\""+ line +"\"],\n"
            if count<5000:datain.write(txt3)
    return #print("--\n",ALL)
cnt=0
SUB = ['a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','w','x','y','z']
for sub in SUB:
    FS = ['a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for L in FS:
        #def savjson(data):
        datain = open("test/a"+sub+L+"json.json","w")
        datain.write("{\n \"conversations\": \n[\n")
        convert("/home/jack/Desktop/PAV/opensubtitles/raw/lines/lines-a"+sub+L+"") 
        datain.write("]}")
        datain.close() 
        file = "test/a"+sub+L+"json.json"
        print(file)
    
    
        data = open(file).readlines()
        newfile = "test/C"+os.path.basename(file)
        clean = open(newfile, "w")
        count = 0
        for line in data:
            count=count+1
            if count<4999:
                #print(line)
                clean.write(line)
            if count>4998:
                line = line.replace("],","]")
                clean.write(line)
                #print(line)

    clean.close()        
