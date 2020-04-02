#
import conv
import sys
args = sys.argv

#prevstr = "T 900 350 -400 50 0 0 0 DA Normal 0 C C"
prevstr = "	1200 900  1550 900 "
nextstr = ""


#nextstr = changeWWLtoLine(prevstr)
#print(nextstr)


# path set
path = args[1]
outputPath = args[2]
print(path)

#open file
readKidat = open(path, "r")
d2wr = open(outputPath, "w")

#read data
wwlflag = False
wblflag = False
for prevstr in readKidat:
    nextstr = conv.changeStoLine(prevstr)
    if not nextstr == "":
        d2wr.write(nextstr)
        continue
    nextstr = conv.changePtoLine(prevstr)
    if not nextstr == "":
        d2wr.write(nextstr)
        continue
    nextstr = conv.changeXtoPin(prevstr)
    if not nextstr == "":
        d2wr.write(nextstr)
        continue
    nextstr = conv.changeTtoText(prevstr)
    if not nextstr == "":
        d2wr.write(nextstr)
        continue

    #return
    d2wr.write("\n")

#close file
readKidat.close()
d2wr.close()

print("write "+outputPath)
