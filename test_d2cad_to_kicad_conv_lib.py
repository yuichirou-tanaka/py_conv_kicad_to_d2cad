import d2cad_to_kicad_conv
import sys
args = sys.argv

# prevstrPin = 'Pin 4810 5250 4750 5250 0'
# prevstrName = 'Name "L1" 4828 5250 70 32792'
# prevstrNo = 'No "1" 4760 5250 70 32778'
# nextstr = ""
# nextstr = d2cad_to_kicad_conv.changePinNameNotoX(prevstrPin, prevstrName, prevstrNo)
# print(nextstr)


prevstrPart = 'Part 6150 4750 6056 4614 6244 4756 0 0 4096 0'
prevstrName = 'Name "AGND" 6150 4650 65 30'
nextstr = ""
nextstr = d2cad_to_kicad_conv.changePartsNametoXF1(prevstrPart, prevstrName)
print(nextstr)
