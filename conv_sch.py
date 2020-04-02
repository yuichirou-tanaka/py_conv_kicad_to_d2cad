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
oldTextNote = ""
for prevstr in readKidat:

    if not oldTextNote == "":
        nextstr = conv.changeSchTextNoteTtoText(oldTextNote, prevstr)
        oldTextNote = ""
        if not nextstr == "":
            d2wr.write(nextstr)
            continue
    
    if prevstr.startswith('Text Notes ') :
        oldTextNote = prevstr
        continue

    if prevstr.startswith("Wire Wire Line"):
        wwlflag = True
        continue
    if wwlflag == True:
        wwlflag = False
        nextstr = conv.changeWWLtoLine(prevstr)
        if not nextstr == "":
            d2wr.write(nextstr)
            continue

    if prevstr.startswith("Wire Bus Line"):
        wblflag = True
        continue
    if wblflag == True:
        wblflag = False
        nextstr = conv.changeWBusLtoLine(prevstr)
        if not nextstr == "":
            d2wr.write(nextstr)
            continue
    #junc
    nextstr = conv.changeConnectToJunc(prevstr)
    if not nextstr == "":
        d2wr.write(nextstr)
        continue
    #return
    #d2wr.write("\n")

#close file
readKidat.close()
d2wr.close()

print("write "+outputPath)
