from os import rename, listdir
import subprocess

import csv

import plotly

foutputname = 'count.txt'
outputfolder = "counts"

dict = {}
list_wanted_language= ["C", "Java","Python" ,"Assembly","SQL","JavaScript","HTML","CSS","Sass"]
fnames = listdir(outputfolder)


# fill dict from data over all counts
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
                dict[words[0]]= {"language": words[0],"subjects": list,"fileCount": dict[words[0]]["fileCount"]+int(words[1]),"code":dict[words[0]]["code"]+int(words[4])}
            else:
                dict[words[0]]= {"language": words[0],"subjects": [name],"fileCount":int(words[1]),"code": int(words[4])}


# Small print to show some of the interessting langs
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


# Write to csv
with open('count.csv', mode='w') as csv_file:
    fieldnames = ['language', 'subjects', 'fileCount', 'code']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for x in dict:
        if x in list_wanted_language:
            writer.writerow(dict[x])
