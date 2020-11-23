
DEF_Y_MAX= 9000
DEF_Y_MOD=-1


# wire 赤い線
#Wire Wire Line
# 4350 2450 4350 3550
def changeLinetoWW(istr):
    rets = ""
    sa = istr.split()
    x1 = int(sa[1])
    y1 = int(sa[2])*DEF_Y_MOD + DEF_Y_MAX
    x2 = int(sa[3])
    y2 = int(sa[4])*DEF_Y_MOD + DEF_Y_MAX
    rets += "Wire Wire Line\n"
    rets += "	" + str(x1) + " "+ str(y1) + " "+ str(x2) + " "+ str(y2) + "\n"
    return rets


#S 0 0 100 -100 0 1 0 N
#S LTX LTY RBX RBY 0 1 0 N
#Line X1 Y1 X2 Y2 8 0 0 0
def changeLinetoS(istr):
    #print("changeStoLine")    
    if not istr.startswith('Line ') :
        #print("no s")
        return ""
    sa = istr.split()
    rets = ""
    ltx = sa[1]
    lty = sa[2]
    rbx = sa[3]
    rby = sa[4]
    rets += "S "+ ltx + " "+ lty + " "+ rbx + " "+ rby + " 0 1 0 N\n"
    return rets

def changeLinetoP(istr):
    #print("changeStoLine")    
    if not istr.startswith('Line ') :
        #print("no s")
        return ""
    sa = istr.split()
    rets = ""
    ltx = sa[1]
    lty = sa[2]
    rbx = sa[3]
    rby = sa[4]
    rets += "P 2 1 1 5 "+ ltx + " "+ lty + " "+ rbx + " "+ rby + "  N\n"
    return rets

def changeLinetoPorWireorWireBus(istr):
    #print("changeStoLine")    
    if not istr.startswith('Line ') :
        #print("no s")
        return ""
    sa = istr.split()
    rets = ""
    ltx = sa[1]
    lty = sa[2]
    rbx = sa[3]
    rby = sa[4]
    rets += "S "+ ltx + " "+ lty + " "+ rbx + " "+ rby + " 0 1 0 N\n"
    return rets
    

    

# 接点
#Connection ~ X Y
#Junc X Y
def changeJuncToConnect(istr):
    rets = ""
    if not istr.startswith('Junc ') :
        #print("no T")
        return ""
    sa = istr.split()
    x = int(sa[1])
    y = int(sa[2])*DEF_Y_MOD + DEF_Y_MAX
    rets += "Connection ~ "+ str(x) + " "+ str(y) + " \n"
    return rets


#DRAW
# pin
# X Es 2 350 0 100 L 50 50 1 1 I
# X Text PinNumber X Y Length UpDownLeftRight 50 50 1 1 I
def changePinNameNotoX(istrPin,isName,isNo):
    #print("changePinNameNotoX")    
    if not istrPin.startswith('Pin ') :
        #print("no Pin ")
        return ""
    if not isName.startswith('Name ') :
        #print("no Name ")
        return ""
    if not isNo.startswith('No ') :
        #print("no No")
        return ""

    #上方向
    #Pin X Y X Y+Len 0
    #Name "FAT" X Y-12 70 282
    #No "1" X Y+50 70 264
    saPin = istrPin.split()
    saNo = isNo.split()
    saName = isName.split()
    pinNumber = saNo[1].replace('"', '')
    #print(saNo) 
    #print(int(pinNumber))    
    sName = saName[1].replace('"', '')
    #print(sName) 
    rets = ""
    pinX = int(saPin[1])
    pinY = int(saPin[2])
    pinX2 = int(saPin[3])
    pinY2 = int(saPin[4])
    width = pinX2 - pinX    
    height = pinY2 - pinY
    #print(" width:"+ str(width) + " height = " + str(height) )

    if width < 0 and height == 0 :
        #print("R")
        iLength = width
        rets += "X "+ sName + " "+ str(pinNumber) + " "+ str(pinX) + " "+ str(pinY) + " "+ str(iLength) + " R 50 50 1 1 I\n"
    elif width > 0 and height == 0 :
        iLength = width
        rets += "X "+ sName + " "+ str(pinNumber) + " "+ str(pinX) + " "+ str(pinY) + " "+ str(iLength) + " L 50 50 1 1 I\n"
        #print("L")
    elif width == 0 and height < 0 :
        iLength = height
        rets += "X "+ sName + " "+ str(pinNumber) + " "+ str(pinX) + " "+ str(pinY) + " "+ str(iLength) + " D 50 50 1 1 I\n"
        #print("D")
    elif width == 0 and height > 0 :
        iLength = height
        rets += "X "+ sName + " "+ str(pinNumber) + " "+ str(pinX) + " "+ str(pinY) + " "+ str(iLength) + " U 50 50 1 1 I\n"
        #print("U")

    return rets

# Part 6150 4750 6056 4614 6244 4756 0 0 4096 0'
# Name "AGND" 6150 4650 65 30'
#F1 "AGND" 0 100 50 H V C CNN
def changePartsNametoXF1(isName):
    print("changePinNameNotoX")    
    # if not isPart.startswith('Part ') :
    #     print("no Part ")
    #     return ""
    if not isName.startswith('Name ') :
        print("no Name ")
        return ""
    saName = isName.split() 
    sName = saName[1]
    rets = "F1 " +  sName + " 0 100 50 H V C CNN"
    return rets