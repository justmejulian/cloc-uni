from os import rename, listdir
import subprocess

foutputname = 'count.txt'
outputfolder = "counts"

dict = {}

fnames = listdir(outputfolder)

for fname in fnames:
    name = fname.split('.')[0]

    crs = open(outputfolder+"/"+fname, "r")

    for raw in crs :
        line = raw.strip()
        if(not line.startswith("-") and not line.startswith("SUM")and not line.startswith("Language")and not line.startswith("github.com")):
            words = line.split()
            if(words[1].isalpha()):
                words.remove(words[1])
                if(words[1].isalpha()):
                    words.remove(words[1])
            if(words[0] in dict):
                list = dict[words[0]]["subjects"]
                list.append(name)
                dict[words[0]]= {"subjects": list,"fileCount": dict[words[0]]["fileCount"]+int(words[1]),"code":dict[words[0]]["code"]+int(words[4])}
            else:
                dict[words[0]]= {"subjects": [name],"fileCount":int(words[1]),"code": int(words[4])}


print("Language:" +'\t\t' + "Lines of Code:")
print("--------------------------------------")
print("C" +'\t\t\t', dict["C"]["code"])
print("Java"+"\t\t\t",dict["Java"]["code"])
print("Python"+"\t\t\t",dict["Python"]["code"])
print("Assembly"+"\t\t",dict["Assembly"]["code"])

print("SQL"+"\t\t\t",dict["SQL"]["code"])


print("JavaScript"+"\t\t",dict["JavaScript"]["code"])

print("HTML"+"\t\t\t",dict["HTML"]["code"])
print("CSS"+"\t\t\t",dict["CSS"]["code"])
print("Sass"+"\t\t\t",dict["Sass"]["code"])
