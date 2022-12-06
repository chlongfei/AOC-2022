file = open("in.txt", "r")
datastr = file.read()

for ch in range(len(datastr)-3):
    string=""
    for a in range(4):
        string+=datastr[ch+a]

    found=0
    for pos in range(4):
        if string.count(datastr[ch+pos]) == 1:
            found+=1

    if found == 4:
        print(string)
        print(ch+14)
        break