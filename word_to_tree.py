#next steps: make a way to have the treedrawer draw the tree from the list.
#perhaps have a second dictionary, where instead of appending 1, it runs draw_river(1)
# or instead of appending [2,1] it runs draw_flap(2) draw_flap(1)

import tkinter

letters ={
    " ":[1],
    "A":[[1],1,[2]],
    'B':[[2,3],1],
    'C':[[2,1],1],
    'D':[[1,2],1],
    'E':[[2,1,1],1],
    'F':[[2,1],1],
    'G':[[2,2],1],
    'H':[[1,1],1,[1]],
    'I':[[1],1],
    'J':[1,[1,1]],    
    'K':[[1],1,[2]],
    'L':[[1,1],1],
    'M':[[2],1,[2]],
    'N':[[1],1,[1,1]],
    'O':[[2,2],1],
    'P':[[3],1],
    'Q':[1,[2,2]],
    'R':[[2],1,[3]],
    'S':[[2],1],
    'T':[1,[1,[0.5,0.5],1],1], #careful with the half units there, idk man
    'U':[[1],1,[1]],
    'V':[[1,1],1],
    'W':[[1,1],1,[1,1]],
    'X':[[2],1,[2]],
    'Y':[[1,[0.5,0.5],1],1],
    'Z':[[2,1],1],
    
#bruh idk about these lowercases
    'a':[[1,1],1],
    'b':[[1,1],1],
    'c':[1,[1]],
    'd':[1,[1,1]],

    'l':[1,[1]],

    'r':[[1],1],
    's':[[1],1],

#seriously, punctuation? oma
    ':':[[1]],
    '?':[[3],1],
    '!':[[2]],
    '<':[1,[2]],
    '>':[[2],1],
    '-':[[1],1],
    '|':[[1],1],
    '/':[[1],1],
    '^':[[2],1],
    '(':[1,[2]],
    ')':[[2],1],

    '1':[[2],1],
    '2':[[3,1],1],
    '3':[[3],1],

    '7':[1,[7]],
    '9':[1,[3]],
    '0':[[2,2],1]
}
    
def convert (word):
    tree = []
    Word = list(word)
    for x in range(0,len(Word)):
        for y in range(0,len(letters[Word[x]])):
            tree.append(letters[Word[x]][y])
    while isinstance(tree[-1],list)==False: #to remove rivers at the end or beginning
        tree.__delitem__(-1)
    while isinstance(tree[0],list)==False:
        tree.__delitem__(0)
    return tree
def modifytree(tree):
    pass #idk i forget what this was supposed to be




"""made a backup copy, i forget why

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
"""





'''
def finddistance(flap1, flap2): #input branchpositions like [0,0] and [2,1,0]
    distance = 0
    index1 = branchpositions.index(flap1)
    index2 = branchpositions.index(flap2)
    
    for x in range(0,len(riverpositions)):
        if ((riverpositions[x]<flap2 and riverpositions[x]>flap1) or (riverpositions[x]>flap2 and riverpositions[x]<flap1))and len(riverpositions[x])<=max(len(flap1),len(flap2)):
            distance += riverlengths[x] #because riverlengths and riverpositions are "synced up"
    distance += branchlengths[index1]+branchlengths[index2]        
    return distance

#for the right side, using spot2
for x in range(0,len(branchcoordinates)):   #each entry will be like (200, 100, 2) for x and y and s
    distance = finddistance(branchpositions[s],branchpositions[branchcoordinates[x][2]])
    while max(abs(600-branchcoordinates[x][0]),abs(spot2-branchcoordinates[x][1])) < distance*500/mingrid and branchpositions[s] != branchpositions[branchcoordinates[x][2]]:
           #the second condition for the black hole function later, when it runs through all the branchcoordinates it will find itself and return distance = flaplength*2
        spot2 += 500/mingrid #move down a unit

for x in range(0,len(branchcoordinates)):   
    distance = finddistance(branchpositions[s],branchpositions[branchcoordinates[x][2]])
    while max(abs(spot3-branchcoordinates[x][0]),abs(600-branchcoordinates[x][1])) < distance*500/mingrid and branchpositions[s] != branchpositions[branchcoordinates[x][2]]:
           #the second condition for the black hole function later, when it runs through all the branchcoordinates it will find itself and return distance = flaplength*2
        spot2 -= 500/mingrid #move down a unit

for x in range(0,len(branchcoordinates)):   
    distance = finddistance(branchpositions[s],branchpositions[branchcoordinates[x][2]])
    while max(abs(100-branchcoordinates[x][0]),abs(spot4-branchcoordinates[x][1])) < distance*500/mingrid and branchpositions[s] != branchpositions[branchcoordinates[x][2]]:
           #the second condition for the black hole function later, when it runs through all the branchcoordinates it will find itself and return distance = flaplength*2
        spot2 -= 500/mingrid #move down a unit



#========== black hole time ============
def blackhole():
    done = False
    while done == False:
        for k in range(0,len(branchcoordinates)): #for each individual branch: (k is the one we're considering to move or not)
            flap = branchcoordinates[k]
            done = True #if this makes it through all the branches without being changed(a flap moves), then we stop
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
                done = False
                if flap[3] == 1:
                    flap[1]+=500/mingrid
                if flap[3] == 2:
                    flap[0]-=500/mingrid
                if flap[3] == 3:
                    flap[1] -=500/mingrid
                if flap[3] == 4:
                    flap[0] += 500/mingrid
            
                        
                        
                    
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

        if flap[3] == 2:
            canvas.create_line(flap[0],flap[1],flap[0]-min(flap[1]-100,radius),flap[1]-min(flap[1]-100,radius),width = 2, fill = 'red')
            canvas.create_line(flap[0],flap[1],flap[0]-min(600-flap[1],radius),flap[1]+min(600-flap[1],radius),width = 2, fill = 'red')
            canvas.create_line(flap[0]-radius,flap[1]-min(flap[1]-100,radius),flap[0]-radius,flap[1]+min(600-flap[1],radius),width = 2, fill = 'blue')
            canvas.create_line(flap[0]-radius,flap[1]-min(flap[1]-100,radius),600,flap[1]-min(flap[1]-100,radius),width=2,fill='blue')
            canvas.create_line(flap[0]-radius,flap[1]+min(600-flap[1],radius),600,flap[1]+min(600-flap[1],radius),width=2,fill='blue')
            
        if flap[3] == 3:
            canvas.create_line(flap[0],flap[1],flap[0]-min(flap[0]-100,radius),flap[1]-min(flap[0]-100,radius),width = 2, fill = 'red') # /
            canvas.create_line(flap[0],flap[1],flap[0]+min(600-flap[0],radius),flap[1]-min(600-flap[0],radius),width = 2, fill = 'red') # \
            canvas.create_line(flap[0]-min(flap[0]-100,radius),flap[1]-radius,flap[0]+min(600-flap[0],radius),flap[1]-radius,width = 2, fill= 'blue')
            canvas.create_line(flap[0]-min(flap[0]-100,radius),flap[1]-min(flap[0]-100,radius),flap[0]-min(flap[0]-100,radius),600,width=2,fill='blue')
            canvas.create_line(flap[0]+min(600-flap[0],radius),flap[1]-min(600-flap[0],radius),flap[0]+min(600-flap[0],radius),600,width=2,fill='blue')

        if flap[3] == 4:
            canvas.create_line(flap[0],flap[1],flap[0]+min(flap[1]-100,radius),flap[1]-min(flap[1]-100,radius),width = 2, fill = 'red')
            canvas.create_line(flap[0],flap[1],flap[0]+min(600-flap[1],radius),flap[1]+min(600-flap[1],radius),width = 2, fill = 'red')
            canvas.create_line(flap[0]+radius,flap[1]+min(flap[1]-100,radius),flap[0]+radius,flap[1]-min(600-flap[1],radius),width = 2, fill = 'blue')
            canvas.create_line(flap[0]+radius,flap[1]+min(flap[1]-100,radius),100,flap[1]+min(flap[1]-100,radius),width=2,fill='blue')
            canvas.create_line(flap[0]+radius,flap[1]-min(600-flap[1],radius),100,flap[1]-min(600-flap[1],radius),width=2,fill='blue')
'''







'''
PLAN:

on the first round, have it run through, but instead of drawing it all there, you store the coordinates in branchcoordinates.
Then, after the black hole goes through and moves the coordinates around, you draw it all.

store the coordinates as their tkinter values, .cp values, or grid values?

'''
