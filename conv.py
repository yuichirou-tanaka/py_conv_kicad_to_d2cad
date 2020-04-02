#
import sys
args = sys.argv

prevstr = "T 900 350 -400 50 0 0 0 DA Normal 0 C C"
nextstr = ""

#S 0 0 100 -100 0 1 0 N
#S LTX LTY RBX RBY 0 1 0 N
#Line X1 Y1 X2 Y2 8 0 0 0
def changeStoLine(istr):
    #print("changeStoLine")    
    if not istr.startswith('S') :
        #print("no s")
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
    #print("changePtoLine")    
    if not istr.startswith('P') :
        #print("no P")
        return ""
    sa = istr.split()
    rets = ""
    lineCnt = int(sa[1])
    for i in range(lineCnt-1):
        idx = i * 2 + 5
        #print(idx)
        ltx = sa[idx + 0]
        lty = sa[idx + 1]
        rbx = sa[idx + 2]
        rby = sa[idx + 3]
        rets += "Line "+ ltx + " "+ lty + " "+ rbx + " "+ rby + " 8 1 0 0 \n"

    return rets

#DRAW
# pin
# X ~ 1 200 -50 100 L 50 50 1 1 I
# X ~ ~ 50 -200 99 U 50 50 1 1 I
# X RST_N 10 900 -1150 200 U 50 50 0 0 U
# X Text PinNumber X Y Length UpDownLeftRight 50 50 1 1 I
def changeXtoPin(istr):
    #print("changeXtoPin")    
    if not istr.startswith('X') :
        #print("no X")
        return ""
    sa = istr.split()
    rets = ""
    name = sa[1]
    pinnumber = sa[2]
    x = int(sa[3])
    y = int(sa[4])
    leng = int(sa[5])
    dir = sa[6]
    if dir == "D":
        #上方向
        #Pin X Y X Y+Len 0
        #Name "FAT" X Y-12 70 282
        #No "1" X Y+50 70 264
        rets += "Pin "+ str(x) + " "+ str(y-leng) + " "+ str(x) + " "+ str(y) + " 0\n"
        if name != "~":
            rets += 'Name "'+ name + '" ' + str(x-12) + " "+ str(y-leng) + " 70 282\n"
        if pinnumber != "~":
            rets += 'No "'+ pinnumber + '" ' + str(x) + " "+ str(y+50-leng) + " 70 264\n"
    elif dir == "U":
        #Pin X Y X Y-Len 0
        #Name "FAT" X Y+12 70 280
        #No "1" X Y-50 70 266
        rets += "Pin "+ str(x) + " "+ str(y+leng) + " "+ str(x) + " "+ str(y) + " 0\n"
        if name != "~":
            rets += 'Name "'+ name + '" ' + str(x) + " "+ str(y+12+leng) + " 70 280\n"
        if pinnumber != "~":
            rets += 'No "'+ pinnumber + '" ' + str(x) + " "+ str(y-50+leng) + " 70 266\n"
    elif dir == "L":
        #右方向
        #Pin X Y X+Len Y 0
        #Name "FAT" X-18 Y 70 26
        #No "1" X+50 Y 70 264
        rets += "Pin "+ str(x-leng) + " "+ str(y) + " "+ str(x) + " "+ str(y) + " 0\n"
        if name != "~":
            rets += 'Name "'+ name + '" ' + str(x-18-leng) + " "+ str(y) + " 70 26\n"
        if pinnumber != "~":
            rets += 'No "'+ pinnumber + '" ' + str(x+100-leng) + " "+ str(y) + " 70 10\n"
    elif dir == "R":
        #Pin X Y X-Len Y 0
        #Name "FAT" X+12 Y 70 24
        #No "1" X-50 Y 70 10
        rets += "Pin "+ str(x+leng) + " "+ str(y) + " "+ str(x) + " "+ str(y) + " 0\n"
        if name != "~":
            rets += 'Name "'+ name + '" ' + str(x+12+leng) + " "+ str(y) + " 70 24\n"
        if pinnumber != "~":
            rets += 'No "'+ pinnumber + '" ' + str(x-50+leng) + " "+ str(y) + " 70 10\n"
    return rets

# T 0 50 -200 50 0 0 0 FA Normal 0 C C
#T 0 100 -200 50 0 0 0 FA Normal 0 C C
#T 0 100 -300 50 0 0 0 FFF Normal 0 C C
#T 900 350 -400 50 0 0 0 DA Normal 0 C C
# Text "test" 2100 7700 70 8
#Text "DA" x y 70 264
#Text "DA" x y 70 520
#Text "DA" x y 70 776
def changeTtoText(istr):
    #print("changeXtoPin")    
    rets = ""
    if not istr.startswith('T') :
        #print("no T")
        return ""
    
    sa = istr.split()
    if sa[1] == "900":
        dir = "R"
    else:
        dir = "D"
    x = int(sa[2])
    y = int(sa[3])
    leng = int(sa[4])
    txt = sa[8]
    if dir == "D":
        rets += 'Text "'+ txt + '" ' + str(x) + " "+ str(y) + " 70 8\n"
    elif dir == "R":
        rets += 'Text "'+ txt + '" ' + str(x) + " "+ str(y) + " 70 264\n"
    return rets

# path set
path = args[1]
outputPath = args[2]
print(path)

#open file
readKidat = open(path, "r")
d2wr = open(outputPath, "w")

#read data
for prevstr in readKidat:
    nextstr = changeStoLine(prevstr)
    if not nextstr == "":
        d2wr.write(nextstr)
        continue
    nextstr = changePtoLine(prevstr)
    if not nextstr == "":
        d2wr.write(nextstr)
        continue
    nextstr = changeXtoPin(prevstr)
    if not nextstr == "":
        d2wr.write(nextstr)
        continue
    nextstr = changeTtoText(prevstr)
    if not nextstr == "":
        d2wr.write(nextstr)
        continue

    d2wr.write("\n")

#close file
readKidat.close()
d2wr.close()

print("write "+outputPath)
