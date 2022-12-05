import re

file = open("in.txt", "r")

rawStack = []

nStacks = 0
nStackIdx = []
nRows=0


def move(qty,f,t):
    
    for i in range(int(qty)):
        container=stack[int(f)-1].pop(0)
        stack[int(t)-1].insert(0,container)
   

# Get num stacks
for ln in file:
    nRows+=1
    if ln == "\n":
        nStacks = int(prevLn[len(prevLn)-3])
        for si in range(nStacks):
            nStackIdx.append(prevLn.find(str(si+1)))
        break
    else:
        prevLn = ln

file.seek(0)
stack=[]

for st in range(nStacks):
    stack.append([])

for row in range(nRows):
    ln = file.readline()
    if ln[1] == "1":
        break
    else:
        for idx,st in enumerate(nStackIdx):
            if ln[st] != " ":
                stack[idx].append(ln[st])

for inst in file:
    if len(inst) > 1:
        # print(stack)
        qty = re.search("(\d+)(?= from)",inst).group()
        fromStack = re.search("(\d+)(?= to)",inst).group()
        toStack = re.search("(\d+)$",inst).group()
        # print("moving ", qty," from ", fromStack, " to ", toStack)
        move(qty,fromStack,toStack)
        # print(stack)


tops=""
for st in range(nStacks):
    tops+=stack[st].pop(0)

print(tops)