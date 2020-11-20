

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
    