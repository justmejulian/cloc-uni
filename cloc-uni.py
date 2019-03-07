from os import rename, listdir
import subprocess

fname = 'dirs.txt'
foutputname = 'count.txt'

outputfolder = "counts"
subprocess.run(['mkdir', outputfolder] )



print ("Read all dirs and count lines of code:")
crs = open(fname, "r")
dirnames = []
for raw in crs :
    dirnames.append(raw.strip())

print ("All repositories:")
print (dirnames)
print ("")

for name in dirnames:
    dirname = name.split("/")
    dirname = dirname[len(dirname)-1]
    print("__________ "+dirname+" __________")

    print ("Cloning:", name)
    subprocess.run(['git','clone', name])
    print ("Counting lines in:", name)
    subprocess.run(['cloc',dirname, "--out", outputfolder+"/"+dirname+".txt"] )
    print ("Removing:", name)
    subprocess.run(['rm',"-f","-r", dirname] )
