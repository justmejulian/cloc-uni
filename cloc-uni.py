from os import rename, listdir
import subprocess

fname = 'dirs.txt'

outputfolder = "counts"
subprocess.run(['mkdir', outputfolder] )


crs = open(fname, "r")
dirnames = []
for raw in crs :
    dirnames.append(raw.strip())

print ("Dirs found:")
print (dirnames)

for name in dirnames:
    dirname = name.split("/")
    dirname = dirname[len(dirname)-1]
    print(dirname)

    print ("Counting lines in...", name)
    subprocess.run(['git','clone', name])
    subprocess.run(['cloc',dirname, "--out", outputfolder+"/"+dirname+".txt"] )
    subprocess.run(['rm',"-f","-r", dirname] )
