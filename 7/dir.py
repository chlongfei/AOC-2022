import re
file = open("in.txt", "r")
raw = file.read()
data = raw.split("\n")

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dir = {}
        self.size = 0

root = Dir("/",None)
curDir = root

first=True

for ln in data:
    # print("Current Dir: ",curDir.name)
    if ln[0] == "$":
        if ln[2:4] == "cd":
            if ln[5:] == "..":
                curDir=curDir.parent
                # print("Going back to ", curDir.name)
            else:
                if not first:
                    curDir=curDir.dir[ln[5:]]
                else:
                    first=False
                # print("Changed Dir to ", curDir.name)

    elif ln[0:3] == "dir":
        curDir.dir[ln[4:]]=Dir(ln[4:],curDir)
    else:
        size = re.search(r"\d+", ln).group()
        curDir.size+=int(size)
        # print("Found file in", curDir.name, " of size ", size)
        # print("Current dir ", curDir.name, "is ", curDir.size)

dirSize=[]

def calculate(directory,dirSizeArr):
    size=directory.size
    for dir in directory.dir.values():
        size+=calculate(dir, dirSizeArr)
    # print("> ",directory.name, "size: ", size)
    dirSize.append(size)
    return size

calculate(root,dirSize)

tot = 0
for dir in dirSize:
    if dir < 100000:
        tot+=dir

print("Space to delete: ",tot)
