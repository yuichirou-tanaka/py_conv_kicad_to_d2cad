#
import d2cad_to_kicad_conv
import sys
args = sys.argv

prevstr = "Line 3240 4780 3200 4740 8 1 0 0"
#prevstr = "	1200 900  1550 900 "
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
oldTextGLabel = ""
oldTextLabel = ""
for prevstr in readKidat:
    print(prevstr)

    if prevstr.startswith("Junc"):
        wwlflag = True

    if wwlflag == True:
        wwlflag = False
        nextstr = d2cad_to_kicad_conv.changeJuncToConnect(prevstr)
        if not nextstr == "":
            d2wr.write(nextstr)
            continue


    if prevstr.startswith("Line"):
        wwlflag = True

    if wwlflag == True:
        wwlflag = False
        nextstr = d2cad_to_kicad_conv.changeLinetoWW(prevstr)
        if not nextstr == "":
            d2wr.write(nextstr)
            continue
    
#close file
readKidat.close()
d2wr.close()

print("write "+outputPath)
