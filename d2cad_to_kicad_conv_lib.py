import d2cad_to_kicad_conv
import sys
args = sys.argv

#prevstr = "Line 3240 4780 3200 4740 8 1 0 0"
prevstr = "Line 3200 4850 3200 4800 8 0 0 0"
nextstr = ""

#nextstr = d2cad_to_kicad_conv.changeLinetoP(prevstr)
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
    nextstr = d2cad_to_kicad_conv.changeLinetoP(prevstr)
    if not nextstr == "":
        d2wr.write(nextstr)
        continue
    #return
    d2wr.write("\n")

#close file
readKidat.close()
d2wr.close()

print("write "+outputPath)
