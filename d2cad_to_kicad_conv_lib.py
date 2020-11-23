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

prevPinFlag = False
prevPinStr = ""
prevNameFlag = False
prevNameStr = ""
prevNoFlag = False

prevPartsFlag = False
for prevstr in readKidat:
    nextstr = d2cad_to_kicad_conv.changeLinetoP(prevstr)
    if not nextstr == "":
        d2wr.write(nextstr)
        continue


    if prevPinFlag == False:
        if prevstr.startswith("Pin "):
            prevPinFlag = True
            prevPinStr = prevstr
            continue
    
    if prevPinFlag==True and prevNameFlag == False:
        if prevstr.startswith("Name "):
            prevNameFlag = True
            prevNameStr = prevstr
            continue
        else:
            prevPinFlag =False

    if prevNoFlag==False and prevPinFlag==True and prevNameFlag == True:
        if prevstr.startswith("No "):
            prevNoFlag = True
        else:
            prevPinFlag = False
            prevNameFlag = False

    if prevNoFlag==True and prevPinFlag==True and prevNameFlag == True:
        nextstr = d2cad_to_kicad_conv.changePinNameNotoX(prevPinStr, prevNameStr, prevstr)
        prevPinFlag = False
        prevNameFlag = False
        prevNoFlag = False
        if not nextstr == "":
            d2wr.write(nextstr)
            continue
    
    prevPinFlag = False
    prevNameFlag = False
    prevNoFlag = False

    if prevstr.startswith('Part ') :
        prevPartsFlag = True
        continue
    if prevPartsFlag == True:
        prevPartsFlag = False
        nextstr = d2cad_to_kicad_conv.changePartsNametoXF1(prevstr)
        if not nextstr == "":
            d2wr.write(nextstr)
            continue


    #return
    d2wr.write("\n")

#close file
readKidat.close()
d2wr.close()

print("write "+outputPath)
