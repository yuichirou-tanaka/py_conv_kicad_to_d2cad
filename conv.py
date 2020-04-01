#prevstr = "S 0 0 100 -100 0 1 0 N"
prevstr = "P 5 0 1 0 0 0 0 -200 200 -200 200 0 0 0 N"
nextstr = ""


#S 0 0 100 -100 0 1 0 N
#S LTX LTY RBX RBY 0 1 0 N
#Line X1 Y1 X2 Y2 8 0 0 0
def changeStoLine(istr):
    print("changeStoLine")    
    if not istr.startswith('S') :
        print("no s")
        return ""
    sa = istr.split()
    rets = ""
    ltx = sa[1]
    lty = sa[2]
    rbx = sa[3]
    rby = sa[4]
    rets += "Line "+ ltx + " "+ lty + " "+ ltx + " "+ rby + " 8 1 0 0 \n"
    rets += "Line "+ ltx + " "+ rby + " "+ rbx + " "+ rby + " 8 1 0 0 \n"
    rets += "Line "+ rbx + " "+ rby + " "+ rbx + " "+ lty + " 8 1 0 0 \n"
    rets += "Line "+ rbx + " "+ lty + " "+ ltx + " "+ lty + " 8 1 0 0 \n"
    return rets
    
#P 5 0 1 0 0 0 0 -200 200 -200 200 0 0 0 N
def changePtoLine(istr):
    print("changePtoLine")    
    if not istr.startswith('P') :
        print("no P")
        return ""
    sa = istr.split()
    rets = ""
    lineCnt = int(sa[1])
    for i in range(lineCnt-1):
        idx = i * 2 + 5
        print(idx)
        ltx = sa[idx + 0]
        lty = sa[idx + 1]
        rbx = sa[idx + 2]
        rby = sa[idx + 3]
        rets += "Line "+ ltx + " "+ lty + " "+ rbx + " "+ rby + " 8 1 0 0 \n"

    return rets

#DRAW
# pin
# X ~ 1 200 -50 100 L 50 50 1 1 I
# X RST_N 10 900 -1150 200 U 50 50 0 0 U
#Pin X Y 200 0 0
#Name "FAT" X-12 Y 70 26
#No "1" X+50 Y 70 8
def changeXtoPin(istr):
    print("changeXtoPin")    
    if not istr.startswith('X') :
        print("no X")
        return

# T 0 50 -200 50 0 0 0 FA Normal 0 C C
#T 0 100 -200 50 0 0 0 FA Normal 0 C C
#T 0 100 -300 50 0 0 0 FFF Normal 0 C C
# Text "test" 2100 7700 70 8
# Text "testa" 2100 7600 70 8
def changeTtoText(istr):
    print("changeXtoPin")    
    if not istr.startswith('T') :
        print("no T")
        return


#nextstr = changeStoLine(prevstr)
nextstr = changePtoLine(prevstr)
print(nextstr)