
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
    