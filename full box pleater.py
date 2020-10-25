"""
You have to both start and end the tree on a flap.
Don't press the river button until you get back to the ground (maybe an indicator?). will cause hecka problems
if you do
Make sure you come back down for every time you go up. Thus the red lines means you haven't come back down :oma:
Don't do things like try to go down first and then go up. bad juju if you do
Make sure to press Start Over when drawing a new tree. It won't clear your tree otherwise, even if the drawing
is empty. However, your cp will still remain, until you click calculate
If you see that it says "faulty solution," click through the other solutions; and if you still don't see anything
you like, then increase the grid size.
bruh something doesn't feel right with this system, i guess there's no way around it
that this is meant for simple trees
subriver adds[length,[]] and index +1 to show we went 1 level deeper
flaps add at the current index level. if index = 0, add directly into main list [[1],[2],[1]]
    if index 1, add to the last item [[1],2,[1,[here]]]
downsub river closes the subriver and index-1.
    if index 1, then close up the last one. adds length to the last item. [1,[flaps],length]
[[1], [1], [1], 4, [4], [4, [[1], [1], [1]], 4], 4, [4, [[1], [1], [1], [1]], 4], [8], 4, [1], [1], [1], [1]]
[[1,1,1],4,[4],[4,[1,1,1],4],4,[4,[1,1,1,1],4],[8],4,[1,1,1,1]]
[[1, 3, 4, 2, 5, 2, 5, 7]]
and maybe make [[1],1,... -> [[2],...
"""
btn_params = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': 'white',
    'bg': '#2E76CF',
    'font': ('arial', 14),
    'relief': 'flat',
    'activebackground': "#173b67"
}

from math import cos as cos
from math import sin as sin
from math import radians as radians
from tkinter import *
master = Tk()
master.configure()
master.title("Boxpleater")
photo = PhotoImage(file="Crane.png")
master.iconphoto(False, photo)
canvas2 = Canvas(master,width=600,height = 450)
canvas2.pack()

progress = []
def start1():
    global Length
    canvas2.create_text(450,30,text="Enter length here")
    Length = Entry(master,bd = 3,width = 10)
    Length.place(x=400,y=45)
    global tree
    global branchcoordinates
    global x
    global y
    global starting_angle
    global angle
    global bigangle
    global cursor
    global index
    global indexlevel
    global maybe #maybe we are making a subsubbranch
    global angletrack
    global blackhole_
    blackhole_ = 1 #by default, we're gonna do blackhole, unless it has a subriver
    index = []
    branchcoordinates = []
    indexlevel = 0
    tree = []
    x = 120
    y = 300
    starting_angle = 120
    angle =120
    bigangle = 110
    maybe = False #big angle = the angle between subbranches
    angletrack = {} #keep track of the angles that you came up at
    cursor = canvas2.create_rectangle(x-2,y-2,x+2,y+2,fill = "red")


def make_flap(length):
    global angle
    #angle = starting_angle
    canvas2.create_line(x,y,x+(length*30*cos(radians(angle))),y-(length*30*sin(radians(angle))), width = 2)
    angle = angle-10
    if indexlevel == 0:
        tree.append([length])
    else:
        dumphere.append([length])
    progress.append("make_flap("+str(length)+")")

    #if we are in subtree, figure out where to put the flaps.
    #else just dump it in the tree
def make_flap2():
    length = eval(Length.get())
    if length > 0:
        make_flap(length)
    else:
        print("please input a positive non-zero number")

def make_river(length):
    if indexlevel == 0:
        global x
        global angle
        global bigangle
        angle = 120
        bigangle = 120 #reset to normal, because means we left the cluster
        global angletrack
        angletrack = {}
        canvas2.create_line(x,y,x+length*30,y, width = 2)
        x += length*30
        tree.append(length)
        global cursor
        canvas2.delete(cursor)
        cursor = canvas2.create_rectangle(x-2,y-2,x+2,y+2,fill = "red")
        progress.append("make_river("+str(length)+")")

    else:
        print("bruh you're still in the subriver, come down first")
def make_river2():
    length = eval(Length.get())
    if length > 0:
        make_river(length)
    else:
        print("please input a positive non-zero number")

def make_subriver(length):
    global bigangle
    global angle
    global y
    global x
    global cursor
    global indexlevel
    global maybe
    #bigangle = 130
    if indexlevel == 0 or maybe == True: #fix later: connect maybe to indexlevel
        bigangle -= 10
        maybe = False
    canvas2.create_line(x,y,x+(length*30*cos(radians(bigangle))),y-(length*30*sin(radians(bigangle))), fill = "red")
    y -= length*30*sin(radians(bigangle))
    x += length*30*cos(radians(bigangle))
    angle = 150 #for the flaps
    canvas2.delete(cursor)
    cursor = canvas2.create_rectangle(x-2,y-2,x+2,y+2,fill = "red")


    global subtree
    global dumphere
    global gobackdown
    if indexlevel == 0: #if this is the first time
        tree.append([length,[]])  #Then to close it, we need to append to to tree[-1]
        subtree = tree[-1] #now we are looking at the list we just made
        dumphere = subtree[1] #this is the empty list, we'll put flaps or nest sublists in there
        gobackdown = tree  #helps to close up
    if indexlevel > 0:  #if indexlevel goes below 0, then idk man
        gobackdown = subtree
        #dumphere.append(length)   dumphere.append([]) i think it should be this but i'm not sure.
        # the down_subriver function is not working completely and i think this is part of the problem.
        # it appears that it's making functional trees, but they aren't exactly as the way i was expecting
        # the trees to be when i wrote the parts that read the trees, so sometimes the cp isn't correct
        dumphere.append([length,[]])#we nest a subsubbranch into the subbranch
        subtree = dumphere[-1]  #from now on we are putting things into this new subsubbranch
        dumphere = subtree[1]

    indexlevel += length
    angletrack[indexlevel] = bigangle

    progress.append("make_subriver("+str(length)+")")
    global blackhole_
    blackhole_ = 0

    #figure find length of the tree so far, make a new list tree[-1] that we're going to
#add to until we come down from the subriver (need that function and button)
#[    [ [] ]] outer brackets are tree. second brackets are subtree. inner brackets are dumphere for new stuff. gobackdown is outside subtree
def make_subriver2():
    length = eval(Length.get())
    if length > 0:
        make_subriver(length)
    else:
        print("please input a positive non-zero number")

def down_subriver(length):
    global angle
    global bigangle
    global y
    global x
    global cursor
    global indexlevel
    global angletrack
    if indexlevel <= 0:
        print("you're on the ground right now oma")
        return #will cut off the rest of the function
    if indexlevel >0 and length > indexlevel:
        length = indexlevel #to prevent going below 0 accidentally
    downangle = angletrack[indexlevel]
    del angletrack[indexlevel]
    canvas2.create_line(x,y,x-(length*30*cos(radians(downangle))),y+(length*30*sin(radians(downangle))), width = 2)
    y += length*30*sin(radians(downangle))
    x -= length*30*cos(radians(downangle))
    angle = 30 #for the flaps on the right side
    canvas2.delete(cursor)
    cursor = canvas2.create_rectangle(x-2,y-2,x+2,y+2,fill = "red")
    global maybe
    maybe = True #maybe we're about to go make a new subsubbranch

    global subtree
    subtree.append(length)
    indexlevel -= length
    global dumphere
    dumphere = subtree
    subtree = gobackdown
    progress.append("down_subriver("+str(length)+")")
def down_subriver2():
    length = eval(Length.get())
    down_subriver(length)

#problem: if you subtree up 1, 1, but go down as 2

#def delete():
    #pass
        #delete the most recent number, on screen. the problem is that in tree,
        #an entire subbranch is one item. will have to delete a bunch of stuff. generator or lambda? :fear:
        #or have a start over button


#treeprogress = str(tree)

def done():
    global progress
    global tree
    #progress.destroy()
    print("Copy and paste this to the main program:")
    print(tree)
    #progress = canvas.create_text(300,375,text = "Tree:" + str(tree))
    progress.delete(0,END)
    progress.insert(0,str(tree))
    #treeprogress.set(str(tree))
    #tk.update()


def start_over():
    canvas2.delete("all")
    start1()
    start2()
    global progress
    progress = []
    """there's a problem right now bc the print button doesn't work after you press start over.
        if you need to print, just type "tree" into the console"""

def go_back():
    canvas2.delete("all")
    start1()
    start2()
    progress.pop()
    progresslength = len(progress) #store this bc it's about to change
    for x in range(0,progresslength):
        eval(progress[0])
        del(progress[0]) #because running each function stored in progress will add more to progress

def start2():
    global done
    flap = Button(master, text="Create Flap", command = make_flap2)
    river = Button(master, text = "Create River", command = make_river2)
    subriver = Button(master, text = "Create Subriver", command = make_subriver2)
    downriver = Button(master, text = "Go back down", command = down_subriver2)
    startover = Button(master,text="Start Over", command = start_over)
    done = Button(master,text="Print code",command = done)
    goback = Button(master,text="undo",command = go_back)

    flap.place(x=400,y=80)
    river.place(x=400,y=110)
    subriver.place(x=400,y=140)
    downriver.place(x=400,y=170)
    startover.place(x=400,y=290)
    goback.place(x = 400,y=260)
    #done.place(x=400,y=320)   #don't need these if have the main program combined, also doesn't seem to work anymore

    #global progress
    #progress = Entry(master, bd = 2)
    #progress.place(x=250,y=375, width = 300)
    #canvas2.create_text(380,360,text="Copy paste this to the main program")

start1()
start2()

#===================================================================================================================================================================================================
#===================================================================================================================================================================================================

"""See the long note at the bottom for full explanation."""

import math
import sys
import random
from tkinter import *
bp_packing = Toplevel()
bp_packing.title("Boxpleater")
photo = PhotoImage(file="Crane.png")
bp_packing.iconphoto(False, photo)
canvas = Canvas(bp_packing,width=900,height=700)
canvas.pack()
entry = Entry(bp_packing,bd = 5)
entry.place(x=620,y=40)
#tree = []   don't need this because have the above input system
def getentry():  #the calculate button
    canvas.delete("all")
    global combinations, successful_starting_positions,branchpositions,branchlengths,riverpositions,riverlengths,blob,combo,C,B,x,y,r,b,mingrid, cp_file,branchcoordinates
    cp_file = []
    combinations = []
    successful_starting_positions = []
    branchpositions = []
    branchlengths = []
    riverpositions = []
    riverlengths = []
    blob = []
    combo = []
    branchcoordinates = []
    C = 0
    B = 0
    x = 0
    y = 0
    r = 0
    b = 0
    mingrid = 0
    global tree
    if entry.get() != "":
        tree = eval(entry.get())
    if isinstance(tree[0],list) == False:
        tree[0] = [tree[0]]
    if isinstance(tree[-1],list)==False:  #needs to start and end on a flap; if they use a river as a flap, then causes problems
        tree[-1] = [tree[-1]]
    entry.delete(0,END)
    canvas.delete("all")
    treepacking(tree)
    #print('YO YO YO BLACK HOLE IS', blackhole_.get())
    #cp_file.append(tree) #for later when we upload it back in, we read first line for the tree. pretty sure non-coordinate text doesn't affect it

enter = Button(bp_packing,text="calculate",command=getentry)
enter.place(x=620,y=80)
'''blackhole_ = IntVar()
blackhole_.set(0)
toggleblackhole = Checkbutton(bp_packing, text = "Black hole", variable = blackhole_,onvalue=1, offvalue=0 )
toggleblackhole.place(x=620,y=105)'''
#canvas.create_text(670,30,text="Enter tree code")

"Everything below here is logic ==========================================================="
#make the global variables
blob=[]
#print("enter tree as a list")
#tree =eval( sys.stdin.readline())
branchpositions = []
branchlengths = []
riverpositions = []
riverlengths = []
#x = 0
#y = 0
r = 0
B = 0
combo = 0 #the first combination we're going to try
C = 0
def blobify(tree):

    #branchify is a subfunction of blobify because it uses recursion.
    #branchify will locate the trees and rivers and stores it in the position lists. also stores lengths in lengths lists
    #then these 4 lists will be used to find the blob list in the main function
    def branchify(tree,index): #index is to keep track of how deep in sublists are we
        for x in range(0,len(tree)): #take each item of the main list. either list or river. x = object in main list
            if isinstance(tree[x],list) == True: #if it's a list and does not have a list
                hassublist = False
                index.append(x)
                for y in range(0,len(tree[x])):   #check if it's a branch cluster or has rivers
                    if isinstance(tree[x][y],list) == True:
                        hassublist = True
                if hassublist == False:  #we want to add these branches (tree[x]) to branchlengths[] and record locations in branchpositions[]
                    #index.append(x)
                    for y in range(0,len(tree[x])):
                        branchlengths.append(tree[x][y])
                        index.append(y)
                        indexcopy = index[:] #idk why but it couldn't directly append index, so we do this
                        branchpositions.append(indexcopy)
                        #print(index)
                        index.pop()
                    index.pop()
                if hassublist == True:
                    branchify(tree[x],index) #this way, you "bring along" the index with you and add onto it
            if isinstance(tree[x],list) == False:
                indexcopy = index[:]
                indexcopy.append(x)
                #indexcopy.append(tree[x])
                riverpositions.append(indexcopy)
                riverlengths.append(tree[x])
            if x == len(tree)-1 and isinstance(tree[x],list)==False: #go back down an index at the end of the list
                index.pop()



    #now to actually make the blob
    r = 0 #what river we're on
    B = 0 #what branch we're on
    for b in range(0,len(branchlengths)-1):  #for each branch: jump to the next one
        print(b)
        bloblength = branchlengths[b]
        while riverpositions[r] > branchpositions[b] and riverpositions[r] < branchpositions[B+1]:
            bloblength = bloblength + riverlengths[r]
            r = r+1
            print(riverpositions[r])
        bloblength = branchlengths[b+1]
        blob.append(bloblength)
    branchify(tree,[])


    def bruh(): #actually makes the blob based on the positions/lengths
        r = 0
        for b in range(0,len(branchlengths)-1):  #for each branch: jump to the next one
            bloblength = branchlengths[b]
            for r in range(0,len(riverlengths)):
                if riverpositions[r] > branchpositions[b] and riverpositions[r] < branchpositions[b+1]:
                    bloblength = bloblength + riverlengths[r]
            bloblength = bloblength + branchlengths[b+1]
            blob.append(bloblength)
            bloblength = 0
        #print(blob)
        bloblength = branchlengths[0] + branchlengths[-1]  #this one is to wrap around
        for r in range(0,len(riverpositions)):
            if len(riverpositions[r]) == 1:
                bloblength = bloblength +riverlengths[r]
        blob.append(bloblength)
    bruh()






#more global variables
successful_starting_positions = []
combinations = []
mingrid = 0
def findgrid(blob):
    global mingrid
    mingrid = sum(blob)/4
    if mingrid != round(mingrid):
        mingrid = math.trunc(mingrid)
        mingrid = mingrid+1
    print("minimum grid size is " + str(mingrid)) #based on edge availability
    if mingrid<max(blob):
        mingrid = max(blob)
        print("adjusted minimum grid size is " + str(mingrid) +". This might get weird") #if one blob side is too large
    return mingrid

def pack(blob):   #generates combinations (arrangement on the edge)
    global mingrid
    done = False
    while done == False:
        for x in range(0,len(blob)):   #x is the side (number) of the blob that we are starting with
            k = x                       #k is the side (number) of the blob that we are looking at rn
            side1 = []
            while sum(side1)<=mingrid-blob[k]:  #if side1 has room for another one
                side1.append(blob[k])
                k=k+1       #k is the length on the string that we are deciding to add or not
                if k == len(blob):      #if we've reached the end, took the last one
                    k=0        #wrap around to the begining of the blob

            side2 = []
            while sum(side2)<=mingrid-blob[k]:
                side2.append(blob[k])
                k = k+1
                if k == len(blob):
                    k=0
            side3 = []
            while sum(side3)<=mingrid-blob[k]:
                if k == x:
                    break
                side3.append(blob[k])
                k = k+1
                if k == len(blob):
                    k=0
            side4 = []
            while sum(side4)<=mingrid-blob[k]:
                if k == x:
                    break   #if it's already got all the sides, then it's done, don't add more
                side4.append(blob[k])
                k = k+1
                if k == len(blob):
                    k=0
            if k == x:
                packing = side1,side2,side3,side4   #tuple, where each element is a list
                newpacking = False
                for X in range(0,len(combinations)): #this tests if the packing is new. Look at existing packings:
                    for y in range(0,4):   #look at the sides of this new packing
                        if packing[y] not in combinations[X]:   #if this side length is not in the already taken packing
                            newpacking = True
                if combinations == [] or newpacking == True: #if it's the first one or it's new
                    if [] not in packing:
                        combinations.append(packing)      #list, where each element is a tuple, and each element of the tuple is a list
                        successful_starting_positions.append(x)
                        #print("STARTING POSITION", successful_starting_positions)
                        done = True #means we found a solution; if it remains false, we increase grid size
        #print("done:",done)
        #print(mingrid)
        if combinations == []: #if we haven't found a solution yet, bump grid size and try again
            mingrid = mingrid+1
            #print("=====error=====")
            #print(":oma: go try treemaker")
            #print("===============")
            #x = 0
            #k = 0
            #done = False
        """for x in range(0,len(combinations)): #sometimes combinations have empty lists, which cause bugs. clean here
            if [] in combinations[x]:
                deletethis.append(combinations[x])
        for x in range(0,len(deletethis)):
            combinations.__delitem__(combinations.index(deletethis[x]))"""


    combinations.append(int(mingrid))     #this is so the drawing function can easily access it
    print("combinations:",combinations)
    return combinations


        # 5 3 , 4 4, 2 2 4, 3 3 2, 神
        #undertrox's [4,3,5,2,6,4,4], this one does not work on default grid so +1

#lang beetle: [[8,4,8],2,[6],[2,[4],[2,[4,1,4],2],[4],2],[6]]

"Everything above here is logic =================================================================="


bump = 0
def Gridbump():
    #print("bump the grid and repack, redraw cp, reset combinations. set C back to 0")
    """ keep the blob and length lists. make the pack() take grid size as input.
        delete old cp
        pack with new grid size
        return C to 0
        drawgrid with new grid size
    """
    global mingrid, C, combinations, successful_starting_positions, bump, cp_file
    cp_file = []
    mingrid += 1
    combinations = []
    successful_starting_positions = []
    C = 0
    pack(blob)
    canvas.delete("all")
    drawgrid(blob, tree, C)
    coverup(C)
    bump += 1  #this lets us prevent going from below the minimum grid size

def gridlower():
    global bump
    if bump > 0:
        global mingrid, C, combinations, successful_starting_positions, cp_file
        cp_file = []
        mingrid -= 1
        combinations = []
        successful_starting_positions = []
        C = 0
        pack(blob)
        canvas.delete("all")
        drawgrid(blob, tree, C)
        coverup(C)
        bump -= 1
    elif bump == 0:
        print("==========================")
        print("oma this is the minimum grid size")

combo = [] #doesn't matter what's in it, the length of it is C but global
def lastsolution():
    C = len(combo)
    print("==============")
    if C > 0:
        global cp_file
        cp_file = []
        canvas.delete("all")
        C -= 1
        combo.__delitem__(0)
        #print("tree",tree)
        #print("blob",blob)
        #print("combinations",combinations)
        print("C",C)
        drawgrid(blob, tree, C)
        coverup(C)
    else:
        print("bruh this is the first solution. Increase grid size if needed.")

def nextsolution():
    print("==============")
    C = len(combo) #something to do with global vs local variables
    if C < len(combinations)-2:
        global cp_file,branchcoordinates
        cp_file = []
        branchcoordinates = []
        canvas.delete("all")
        C += 1
        combo.append("bruh") #can't seem to directly change it but we can add to it. combo and C are the same. Bruh ok i didn't realize until after but i could have used global
        print("C",C)
        drawgrid(blob, tree, C)
        coverup(C)
    else:
        print("bruh no more solutions. Increase grid size if needed.")


from tkinter import*
import tkinter.filedialog
boi = Tk()
boi.withdraw()
def file_save():
    filename = tkinter.filedialog.asksaveasfile(mode='w+', defaultextension=".cp",parent = boi)
    if filename is None: # asksaveasfile return `None` if dialog closed with "cancel".
        boi.withdraw()
        return
    for x in range(0,len(cp_file)):
        #print(cp_file[x])
        filename.write(str(cp_file[x])+"\n")

    filename.close()
    boi.withdraw()



gridbump = Button(bp_packing, text = "increase grid size", command=Gridbump)
gridlower = Button(bp_packing, text = "lower grid size", command=gridlower)
nextsolution = Button(bp_packing,text="next solution",command=nextsolution)
lastsolution = Button(bp_packing,text = "previous solution",command=lastsolution)
filesave = Button(bp_packing, text = "Save as .cp file", command = file_save)
#canvas.pack()

#canvas.create_rectangle(100,600,600,100,outline = "black", width = 2)
top = 600
right = 600
bottom = 100
left = 100

def finddistance(flap1, flap2): #input branchpositions like [0,0] and [2,1,0]
    distance = 0
    index1 = branchpositions.index(flap1)
    index2 = branchpositions.index(flap2)

    for x in range(0,len(riverpositions)):
        if ((riverpositions[x]<flap2 and riverpositions[x]>flap1) or (riverpositions[x]>flap2 and riverpositions[x]<flap1)) and len(riverpositions[x])<max(len(flap1),len(flap2)):
            distance += riverlengths[x] #because riverlengths and riverpositions are "synced up"
    distance += branchlengths[index1]+branchlengths[index2]
    return distance

EPS = 1e-12 # Very small number, 10^(-12), to take care of roundoff error
def equal(a, b):
  return abs(a - b) < EPS
def less(a, b):
  return (a < b) and not equal(a, b)
def lessequal(a, b):
  return (a < b) or equal(a, b)


def blackhole():
    consec_no_movement = 0
    movedin = 0 #how many units in has it moved in. it can't move more than the length of the grid
    while consec_no_movement < len(branchcoordinates):
        for k in range(0,len(branchcoordinates)): #for each individual branch: (k is the one we're considering to move or not)
            flap = branchcoordinates[k]
            move = True #we assume we're gonna move it, but if one flap says no, then we don't
            for n in range(0,len(branchcoordinates)):#run through distances against all of the others
                testflap = branchcoordinates[n]
                distance = finddistance(branchpositions[flap[2]],branchpositions[testflap[2]])*500/mingrid #the minimum distance they can be

                if flap[3] == 1 and k!=n: #if this is the top side, and don't test against self:
                    if less(max(abs(flap[0]-testflap[0]),abs(flap[1]-testflap[1])-500/mingrid),distance):
                        move = False #something might be wrong with the -500/mingrid part
                if flap[3] == 2 and k!=n: #if this is the right side:
                    if less(max(abs(flap[0]-testflap[0])-500/mingrid,abs(flap[1]-testflap[1])),distance):
                        move = False
                if flap[3] == 3 and k!=n: #if this is the bottom side:
                    if less(max(abs(flap[0]-testflap[0]),abs(flap[1]-testflap[1])-500/mingrid),distance):
                        move = False
                if flap[3] == 4 and k!=n: #if this is the left side:
                    if less(max(abs(flap[0]-testflap[0])-500/mingrid,abs(flap[1]-testflap[1])),distance):
                        move = False
            if move==True:
                consec_no_movement = 0
                if flap[3] == 1:
                    flap[1]+=500/mingrid
                if flap[3] == 2:
                    flap[0]-=500/mingrid
                if flap[3] == 3:
                    flap[1] -=500/mingrid
                if flap[3] == 4:
                    flap[0] += 500/mingrid
            else:
                consec_no_movement += 1
        movedin += 1
        if movedin > mingrid:
            consec_no_movement = len(branchcoordinates) #break the loop, we're done.

def cp(tk):  #convert tk coordinates into .cp coordinates
	return (tk-100)*400/500-200

def drawcoordinates(branchcoordinates):
    for f in range(0,len(branchcoordinates)):
        flap = branchcoordinates[f]

        radius = flap[4] #in tkinter units

        if flap[3] == 1:
            canvas.create_line(flap[0],flap[1],flap[0]-min(flap[0]-100,radius),flap[1]+min(flap[0]-100,radius),width = 2, fill = 'red') # /
            canvas.create_line(flap[0],flap[1],flap[0]+min(600-flap[0],radius),flap[1]+min(600-flap[0],radius),width = 2, fill = 'red') # \
            canvas.create_line(flap[0]-min(flap[0]-100,radius),flap[1]+radius,flap[0]+min(600-flap[0],radius),flap[1]+radius,width = 2, fill= 'blue')
            canvas.create_line(flap[0]-min(flap[0]-100,radius),flap[1]+min(flap[0]-100,radius),flap[0]-min(flap[0]-100,radius),100,width=2,fill='blue')
            canvas.create_line(flap[0]+min(600-flap[0],radius),flap[1]+min(600-flap[0],radius),flap[0]+min(600-flap[0],radius),100,width=2,fill='blue')

            cp_file.append("2 "+str(cp(flap[0]))+" "+str(cp(flap[1]))+" "+str(cp(flap[0]-min(flap[0]-100,radius)))+" "+str(cp(flap[1]+min(flap[0]-100,radius)))) # /
            cp_file.append("2 "+str(cp(flap[0]))+" "+str(cp(flap[1]))+" "+str(cp(flap[0]+min(600-flap[0],radius)))+" "+str(cp(flap[1]+min(600-flap[0],radius)))) # \
            cp_file.append("3 "+str(cp(flap[0]-min(flap[0]-100,radius)))+" "+str(cp(flap[1]+radius))+" "+str(cp(flap[0]+min(600-flap[0],radius)))+" "+str(cp(flap[1]+radius)))
            cp_file.append("3 "+str(cp(flap[0]-min(flap[0]-100,radius)))+" "+str(cp(flap[1]+min(flap[0]-100,radius)))+" "+str(cp(flap[0]-min(flap[0]-100,radius)))+" "+str(cp(100)))
            cp_file.append("3 "+str(cp(flap[0]+min(600-flap[0],radius)))+" "+str(cp(flap[1]+min(600-flap[0],radius)))+" "+str(cp(flap[0]+min(600-flap[0],radius)))+" "+str(cp(100)))



        if flap[3] == 2:
            canvas.create_line(flap[0],flap[1],flap[0]-min(flap[1]-100,radius),flap[1]-min(flap[1]-100,radius),width = 2, fill = 'red')
            canvas.create_line(flap[0],flap[1],flap[0]-min(600-flap[1],radius),flap[1]+min(600-flap[1],radius),width = 2, fill = 'red')
            canvas.create_line(flap[0]-radius,flap[1]-min(flap[1]-100,radius),flap[0]-radius,flap[1]+min(600-flap[1],radius),width = 2, fill = 'blue')
            canvas.create_line(flap[0]-radius,flap[1]-min(flap[1]-100,radius),600,flap[1]-min(flap[1]-100,radius),width=2,fill='blue')
            canvas.create_line(flap[0]-radius,flap[1]+min(600-flap[1],radius),600,flap[1]+min(600-flap[1],radius),width=2,fill='blue')

            cp_file.append("2 "+str(cp(flap[0]))+" "+str(cp(flap[1]))+" "+str(cp(flap[0]-min(flap[1]-100,radius)))+" "+str(cp(flap[1]-min(flap[1]-100,radius))))
            cp_file.append("2 "+str(cp(flap[0]))+" "+str(cp(flap[1]))+" "+str(cp(flap[0]-min(600-flap[1],radius)))+" "+str(cp(flap[1]+min(600-flap[1],radius))))
            cp_file.append("3 "+str(cp(flap[0]-radius))+" "+str(cp(flap[1]-min(flap[1]-100,radius)))+" "+str(cp(flap[0]-radius))+" "+str(cp(flap[1]+min(600-flap[1],radius))))
            cp_file.append("3 "+str(cp(flap[0]-radius))+" "+str(cp(flap[1]-min(flap[1]-100,radius)))+" "+str(cp(600))+" "+str(cp(flap[1]-min(flap[1]-100,radius))))
            cp_file.append("3 "+str(cp(flap[0]-radius))+" "+str(cp(flap[1]+min(600-flap[1],radius)))+" "+str(cp(600))+" "+str(cp(flap[1]+min(600-flap[1],radius))))


        if flap[3] == 3:
            canvas.create_line(flap[0],flap[1],flap[0]-min(flap[0]-100,radius),flap[1]-min(flap[0]-100,radius),width = 2, fill = 'red') # /
            canvas.create_line(flap[0],flap[1],flap[0]+min(600-flap[0],radius),flap[1]-min(600-flap[0],radius),width = 2, fill = 'red') # \
            canvas.create_line(flap[0]-min(flap[0]-100,radius),flap[1]-radius,flap[0]+min(600-flap[0],radius),flap[1]-radius,width = 2, fill= 'blue')
            canvas.create_line(flap[0]-min(flap[0]-100,radius),flap[1]-min(flap[0]-100,radius),flap[0]-min(flap[0]-100,radius),600,width=2,fill='blue')
            canvas.create_line(flap[0]+min(600-flap[0],radius),flap[1]-min(600-flap[0],radius),flap[0]+min(600-flap[0],radius),600,width=2,fill='blue')

            cp_file.append("2 "+str(cp(flap[0]))+" "+str(cp(flap[1]))+" "+str(cp(flap[0]-min(flap[0]-100,radius)))+" "+str(cp(flap[1]-min(flap[0]-100,radius)))) # /
            cp_file.append("2 "+str(cp(flap[0]))+" "+str(cp(flap[1]))+" "+str(cp(flap[0]+min(600-flap[0],radius)))+" "+str(cp(flap[1]-min(600-flap[0],radius)))) # \
            cp_file.append("3 "+str(cp(flap[0]-min(flap[0]-100,radius)))+" "+str(cp(flap[1]-radius))+" "+str(cp(flap[0]+min(600-flap[0],radius)))+" "+str(cp(flap[1]-radius)))
            cp_file.append("3 "+str(cp(flap[0]-min(flap[0]-100,radius)))+" "+str(cp(flap[1]-min(flap[0]-100,radius)))+" "+str(cp(flap[0]-min(flap[0]-100,radius)))+" "+str(cp(600)))
            cp_file.append("3 "+str(cp(flap[0]+min(600-flap[0],radius)))+" "+str(cp(flap[1]-min(600-flap[0],radius)))+" "+str(cp(flap[0]+min(600-flap[0],radius)))+" "+str(cp(600)))



        if flap[3] == 4:
            canvas.create_line(flap[0],flap[1],flap[0]+min(flap[1]-100,radius),flap[1]-min(flap[1]-100,radius),width = 2, fill = 'red')
            canvas.create_line(flap[0],flap[1],flap[0]+min(600-flap[1],radius),flap[1]+min(600-flap[1],radius),width = 2, fill = 'red')
            canvas.create_line(flap[0]+radius,flap[1]+min(flap[1]-100,radius),flap[0]+radius,flap[1]-min(600-flap[1],radius),width = 2, fill = 'blue')
            canvas.create_line(flap[0]+radius,flap[1]+min(flap[1]-100,radius),100,flap[1]+min(flap[1]-100,radius),width=2,fill='blue')
            canvas.create_line(flap[0]+radius,flap[1]-min(600-flap[1],radius),100,flap[1]-min(600-flap[1],radius),width=2,fill='blue')

            cp_file.append("2 "+str(cp(flap[0]))+" "+str(cp(flap[1]))+" "+str(cp(flap[0]+min(flap[1]-100,radius)))+" "+str(cp(flap[1]-min(flap[1]-100,radius))))
            cp_file.append("2 "+str(cp(flap[0]))+" "+str(cp(flap[1]))+" "+str(cp(flap[0]+min(600-flap[1],radius)))+" "+str(cp(flap[1]+min(600-flap[1],radius))))
            cp_file.append("3 "+str(cp(flap[0]+radius))+" "+str(cp(flap[1]+min(flap[1]-100,radius)))+" "+str(cp(flap[0]+radius))+" "+str(cp(flap[1]-min(600-flap[1],radius))))
            cp_file.append("3 "+str(cp(flap[0]+radius))+" "+str(cp(flap[1]+min(flap[1]-100,radius)))+" "+str(cp(100))+" "+str(cp(flap[1]+min(flap[1]-100,radius))))
            cp_file.append("3 "+str(cp(flap[0]+radius))+" "+str(cp(flap[1]-min(600-flap[1],radius)))+" "+str(cp(100))+" "+str(cp(flap[1]-min(600-flap[1],radius))))






def grid(size):
    step = 500/size
    for x in range(1,size):
        canvas.create_line(100+x*step, 100, 100+x*step, 600, width = 0.5, fill = "gray")    #vertical line
        canvas.create_line(100,100+x*step, 600, 100+x*step, width = 0.5, fill = "gray")    #horizontal line
s=0
def drawgrid(blob,tree,C):  #blob will be packed, then used for markings and grid. tree is needed for square packing
    gridbump.place(x=700,y=130)
    gridlower.place(x=700,y=160)
    nextsolution.place(x=700,y=190)
    lastsolution.place(x=700,y=220)

    filesave.place(x=700,y=280)

    canvas.create_rectangle(100,600,600,100,outline = "black", width = 2)
    mingrid = combinations[-1]
    grid(mingrid)

    packing1 = combinations[C]
    packing1side1 = packing1[0]  #is a list of the distances along this side
    packing1side2 = packing1[1]
    packing1side3 = packing1[2]
    packing1side4 = packing1[3]

    gridunit = 400/mingrid #this is for orihime

    global branchcoordinates
    branchcoordinates = [] #each entry will be (x,y). saved as (spot1,100,s) for example.

    #s: where in branchlengths we are drawing. increase 1 every time, then wrap around when reach the end.
    global s
    s = successful_starting_positions[C]#################################change the 0 here for next solution#####################################
    def drawtopmarks(): #side 1, draws without regard for constraints.
        #s = successful_starting_positions[C]
        global s
        spot1 = 100 #we add to this variable so the marks build off the previous
        spot1cp = -200

        spot1 = 600-(500/mingrid)*sum(packing1side1)


        #print(packing1side1)
        for x in range(0,len(packing1side1)+1): #for all the flaps in this blobside
            if s >= len(branchlengths) :
                s = 0
                radius = branchlengths[s]*(500/mingrid)
            else:
                radius = branchlengths[s]*(500/mingrid) ########################
            '''
            cp_file.append("2 "+str(spot1cp-radius*(400/500))+" "+str(-200+radius*(400/500))+" "+str(spot1cp)+" -200")
            cp_file.append("2 "+str(spot1cp+radius*(400/500))+" "+str(-200+radius*(400/500))+" "+str(spot1cp)+" -200")
            cp_file.append("3 "+str(spot1cp-radius*(400/500))+" "+str(-200+radius*(400/500))+" "+str(spot1cp-radius*(400/500))+" -200")
            cp_file.append("3 "+str(spot1cp+radius*(400/500))+" "+str(-200+radius*(400/500))+" "+str(spot1cp+radius*(400/500))+" -200")
            cp_file.append("3 "+str(spot1cp-radius*(400/500))+" "+str(-200+radius*(400/500))+" "+str(spot1cp+radius*(400/500))+" "+str(-200+radius*(400/500)))'''

            branchcoordinates.append([spot1,100,s,1,radius])  #where the branch is, and then which branch it was, and that it was the top side

            s = s+1
            if x in range(0,len(packing1side1)):
                spot1 = spot1+ (500/mingrid)*packing1side1[x]
                spot1cp += gridunit*packing1side1[x]
        global top
        top = spot1

    global faulty
    faulty = False #faulty is if a flap gets pushed off the edge

    def drawrightmarks(): #side2
        #s = successful_starting_positions[C]+len(packing1side1)
        global s, faulty
        spot2 = 100
        spot2 = 600-(500/mingrid)*sum(packing1side2)
        spot2cp = -200
        s-=1
        for x in range(0,len(packing1side2)+1):
            if s >= len(branchlengths) :
                s = 0
                radius = branchlengths[s]*(500/mingrid)
            else:
                radius = branchlengths[s]*(500/mingrid) ########################
            canvas.create_line(600,spot2,615,spot2, width = 3, fill = "red")
            if x>0:
                #print(s, 'AT', spot2)
                for test in range(0,len(branchcoordinates)):   #each entry will be like (200, 100, 2) for x and y and s. test is the flap wer're testing against
                    distance = finddistance(branchpositions[s],branchpositions[branchcoordinates[test][2]])
                    while less(max(abs(600-branchcoordinates[test][0]),abs(spot2-branchcoordinates[test][1])), distance*500/mingrid) and branchpositions[s] != branchpositions[branchcoordinates[test][2]]:
                           #the second condition for the black hole function later, when it runs through all the branchcoordinates it will find itself and return distance = flaplength*2
                        #print("bruh bruh! it's spot",s,"compared to", x,"distance",distance,spot2)
                        spot2 += 500/mingrid #move down a unit
                        #note: the case of [[6, 1, 6, 1, 6, 1, 6, 1]] will move down unecessarily. perhaps black hole would fix
                '''         
                cp_file.append("2 200 "+str(spot2cp)+" "+str(200-radius*400/500)+" "+str(spot2cp+radius*(400/500))) #the ridges
                cp_file.append("2 200 "+str(spot2cp)+" "+str(200-radius*400/500)+" "+str(spot2cp-radius*(400/500)))
                cp_file.append("3 200 "+str(spot2cp-radius*(400/500))+" "+str(200-radius*(400/500))+" "+str(spot2cp-radius*(400/500))) #the hinges
                cp_file.append("3 200 "+str(spot2cp+radius*(400/500))+" "+str(200-radius*(400/500))+" "+str(spot2cp+radius*(400/500)))
                cp_file.append("3 "+str(200-radius*(400/500))+" "+str(spot2cp+radius*(400/500))+" "+str(200-radius*(400/500))+" "+str(spot2cp-radius*(400/500)))'''

                branchcoordinates.append([600,spot2,s,2,radius])  #where the branch is, and then which branch it was, and that it was the right side

            s = s+1
            if x in range(0,len(packing1side2)):
                spot2 = spot2+ (500/mingrid)*packing1side2[x]
                spot2cp += gridunit*packing1side2[x]
        global right  #for drawing the yellow marks
        right = spot2
        if spot2>600:
            faulty = True

    def drawbottommarks(): #side3
        global bottom, faulty
        #s = successful_starting_positions[C]+len(packing1side1)+len(packing1side2)
        global s
        s-=1
        spot3 = 600
        spot3 = 100 + (500/mingrid)*sum(packing1side3)
        spot3cp = 200
        for x in range(0,len(packing1side3)+1):
            if s >= len(branchlengths) :
                s = 0
                radius = branchlengths[s]*(500/mingrid)
            else:
                radius = branchlengths[s]*(500/mingrid) ########################
            canvas.create_line(spot3, 600, spot3, 615, width = 3, fill = "red")
            if x>0:
                for test in range(0,len(branchcoordinates)):
                    distance = finddistance(branchpositions[s],branchpositions[branchcoordinates[test][2]])
                    while less(max(abs(spot3-branchcoordinates[test][0]),abs(600-branchcoordinates[test][1])), distance*500/mingrid) and branchpositions[s] != branchpositions[branchcoordinates[test][2]]:
                           #the second condition for the black hole function later, when it runs through all the branchcoordinates it will find itself and return distance = flaplength*2
                        #print(test, 'which is', branchcoordinates[test],distance)
                        spot3 -= 500/mingrid #move down a unit
                '''        
                cp_file.append("2 "+str(spot3cp-radius*(400/500))+" "+str(200-radius*(400/500))+" "+str(spot3cp)+" 200")
                cp_file.append("2 "+str(spot3cp+radius*(400/500))+" "+str(200-radius*(400/500))+" "+str(spot3cp)+" 200")
                cp_file.append("3 "+str(spot3cp-radius*(400/500))+" "+str(200-radius*(400/500))+" "+str(spot3cp-radius*(400/500))+" 200")
                cp_file.append("3 "+str(spot3cp+radius*(400/500))+" "+str(200-radius*(400/500))+" "+str(spot3cp+radius*(400/500))+" 200")
                cp_file.append("3 "+str(spot3cp-radius*(400/500))+" "+str(200-radius*(400/500))+" "+str(spot3cp+radius*(400/500))+" "+str(200-radius*(400/500)))'''

                branchcoordinates.append([spot3,600,s,3,radius])  #where the branch is, and then which branch it was, and that it was the bottom side

            s = s+1
            if x in range(0,len(packing1side3)):
                spot3 = spot3-(500/mingrid)*packing1side3[x]
                spot3cp -= gridunit*packing1side3[x]
        bottom = spot3
        if spot3<100:
            faulty = True


    def drawleftmarks(): #side4
        global faulty
        #s = successful_starting_positions[C]+len(packing1side1)+len(packing1side2)+len(packing1side3)
        global s
        s-=1
        spot4 = 600
        spot4cp = 200
        for x in range(0,len(packing1side4)):
            if s >= len(branchlengths):
                s = 0
                radius = branchlengths[s]*(500/mingrid)   #should it be +C or plus the successfull starting position?
            else:
                radius = branchlengths[s]*(500/mingrid) ########################
            canvas.create_line(100,spot4,85,spot4, width = 3, fill = "red")
            if x>0:

                for test in range(0,len(branchcoordinates)):
                    distance = finddistance(branchpositions[s],branchpositions[branchcoordinates[test][2]])
                    while less(max(abs(100-branchcoordinates[test][0]),abs(spot4-branchcoordinates[test][1])), distance*500/mingrid) and branchpositions[s] != branchpositions[branchcoordinates[test][2]]:
                           #the second condition for the black hole function later, when it runs through all the branchcoordinates it will find itself and return distance = flaplength*2
                        spot4 -= 500/mingrid #move down a unit
                '''        
                cp_file.append("2 -200 "+str(spot4cp)+" "+str(-200+radius*400/500)+" "+str(spot4cp+radius*(400/500))) #the ridges
                cp_file.append("2 -200 "+str(spot4cp)+" "+str(-200+radius*400/500)+" "+str(spot4cp-radius*(400/500)))
                cp_file.append("3 -200 "+str(spot4cp-radius*(400/500))+" "+str(-200+radius*(400/500))+" "+str(spot4cp-radius*(400/500))) #the hinges
                cp_file.append("3 -200 "+str(spot4cp+radius*(400/500))+" "+str(-200+radius*(400/500))+" "+str(spot4cp+radius*(400/500)))
                cp_file.append("3 "+str(-200+radius*(400/500))+" "+str(spot4cp+radius*(400/500))+" "+str(-200+radius*(400/500))+" "+str(spot4cp-radius*(400/500)))'''

                branchcoordinates.append([100,spot4,s,4,radius])  #where the branch is, and then which branch it was

            s = s+1
            if x in range(0,len(packing1side4)):
                spot4 = spot4- (500/mingrid)*packing1side4[x]
                spot4cp -= gridunit*packing1side4[x]
        global left
        left = spot4
        if spot4 <100:
            faulty = True
            #the left side is a little bit different, could be buggy

    drawtopmarks()
    drawrightmarks()
    drawbottommarks() #doesn't really draw, tbh
    drawleftmarks()


    if blackhole_:
        blackhole()
    drawcoordinates(branchcoordinates)


    cp_file.append("1 -200 -200 -200 200")
    cp_file.append("1 200 -200 200 200")
    cp_file.append("1 -200 -200 200 -200")
    cp_file.append("1 -200 200 200 200")

    if faulty == True:
        canvas.create_text(350,350, text = "WARNING: faulty solution")
    if len(combinations)==2 and faulty == True:
        print(mingrid,'mingrid')
        Gridbump()  #it won't stop you from lowering grid size and seeing the faulty solutions
        global bump
        bump += 1




def coverup(C): #coverup mess outside the square
    canvas.create_rectangle(0,0,710,99,fill = "white",width = 0)
    canvas.create_rectangle(0,601,710,710, fill = "white",width = 0)
    canvas.create_rectangle(0,0,99,710,fill = "white",width = 0)
    canvas.create_rectangle(601,0,1110,710,fill = "white",width = 0)
    canvas.create_rectangle(100,100,600,600,width = 2)
    canvas.create_text(350,33,text="solution "+str(C+1)+" of "+str(len(combinations)-1))
    canvas.create_text(350,66,text="grid size: " + str(combinations[-1]))
    #canvas.create_text(350,640,text="Created by Brandon Wong")
    '''canvas.create_line(bottom,610, 100, 610, width = 4, fill = "orange")
    canvas.create_line(610,right, 610, 600, width = 4, fill = "orange")
    canvas.create_line(top,90, 600, 90, width = 4, fill = "orange")
    canvas.create_line(90,left+(branchlengths[successful_starting_positions[C]]*500/mingrid),90,100+(branchlengths[successful_starting_positions[C]]*500/mingrid), width = 4, fill = "orange")
    '''
#used to be branchlengths[0]


#C = 0 #C is the solution that we draw

def treepacking(tree):   #combines everything
    print("tree:",tree)
    blobify(tree)       #adds things to the empty lists
    print("blob: ",blob)
    global mingrid
    mingrid = findgrid(blob)
    #print("minimum grid size: ",mingrid)
    combinations = pack(blob)
    #print("practical grid size is " + str(mingrid)) #why says 0?
    #print("combinations:",combinations) the actual print is in pack()
    #print("branch positions:", branchpositions) #these three are global variables, modified by branchify(tree)
    print("branch lengths:", branchlengths)
    #print("river positions:",riverpositions)
    drawgrid(blob,tree,C) #the 0 means first solution only. Soon, we can loop to show all solutions
    coverup(C)
#treepacking(tree)

if len(successful_starting_positions) > 1:
    if successful_starting_positions[0] == successful_starting_positions[1]:
        successful_starting_positions.__delitem__(0)



#treepacking([[random.randrange(1,5),random.randrange(3,7),random.randrange(1,5)],random.randrange(1,5),[5,[random.randrange(1,6),random.randrange(1,6)],5],random.randrange(1,5),[random.randrange(4,9)]])

"""
This is Boxpleater, a program to help in the origami design process. You input the tree you want
    with the lengths in grid units, and Boxpleater will generate a packing for you. Boxpleater's
    "optimization" considers the lowest grid size for the given tree to be the most efficient, so
    you do not need to input the grid size you want.
One important disclaimer is that Boxpleater will not pack any flaps as center flaps. A few reasons:
    First, Boxpleater was created in the context of 2d color change design, specifically the
        Buntaran-Wong-Minh "string" method that does not use center flaps.
    Second, centerflaps are usually inefficient and annoying to fold. Not only does it take up
        twice as much space as an edge flap, but also because of the centerflap's
        strange position and thickness, often times you don't get
        the whole thing. For example, if you plan for a 4unit long centerflap, it takes 64 square
        units, and you really only get 3 units "sticking out." A 3 unit edge flap (18 units) is
        much better.
    Third, I don't have an algorithm for center flaps.
Although many designers use box pleating, Boxpleater is more of a tool than a replacement for
    designers. There are many design aspects that Boxpleater can't do, such as texture, levelshifters,
    or other unaxial bp structures--much less shaping, and all that is left to humans. After all,
    origami is an art, and the program can only do the math.
THEORY EXPLANATION
1. tree
2. string figure (skipped)
3. blob
4. packed square that tracks vertices
5. the square and vertices on the edge
6. flaps move in (black hole)
7. packing is drawn
1. The tree is input numerically by writing out a list of lists. rivers are integers
    on their own, are not in a list (kinda. it's complicated)
2. skip. String figures are more to show humans how the blob and tree are related.
3. the blob figure is made by blobify(tree) and caluclates the distances between the
    tips of adjacent branches as paths along the tree. It is circular, meaning it also calculates
    the distance from the last branch back to the first
4. The minimum grid size is calculated based off the blob figure. The program
    tries to inscribe a square of the given grid size into the blob figure.
    If it doesn't work, the program increases the grid size and tries again. There
    may be multiple solutions.
5. the vertices are marked based on the packing along the 4 sides. The program starts packing
    in the top left and goes clockwise. For every flap placed, the program checks to make sure that
    the distance from the current flap to every already-placed flap is greater than or equal to
    the two flaps' distance along the tree, and if this constraint is not met, it will move the
    current flap until it is so. This could result in a flap being pushed off the edge, which
    the program responds by moving on to the next solution or increasing the grid size.
6. Once the flaps are all positioned along the edge, each flap (starting in top left
    and going clockwise) will try to move in towards the center, as if sucked
    by a "black hole." They will take turns moving in one unit at a time, until they can
    no longer move without breaking the distance constraint. This should make the rivers easier for the user to see.
    then a square and
    ridge creases are drawn around the vertex with "radius" being the flap length for
    that vertex. If there are wasted edges, the flaps on that edge might be able to shift.
STILL NEEDS TO BE DONE
=========
fix the situations that print "this might get weird". example: treepacking([[1,1],2,[3,1]]). This one has empty lists
show rivers
can draw some of the axial and axial+1 creases (but how to account for mv?)
can do bw at least by drawing concentric squares along the grid, but only if can shift flaps
Things Boxpleater can't do (yet):
    symmetry
    draw rivers
    shift flaps  (move function?)
    use center flaps to fill in gaps
    draw the cp based on packing (axial and axial+1)
    draw it mv
    pack optimally with the center flaps taken into account
    figure out best way to cut shape into tree (2d design, vector input?)
        otpimize edge: minimum total branch length sum
        optimize paper: minimum average branch length (what about rivers?)
        connect these two would be op
    
"""
#[[1],[1,[1],[1,[1,1],1],1],1,[1],[1,[1],[1,[1,1],1],1],[1]] multiple solutions
#[[1],[1,[1,1],1],1,[1],[1,[1],[1,[1,1],1],1],[1]]

master.mainloop()

from word_to_tree import *
