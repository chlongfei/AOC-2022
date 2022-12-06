file = open("in.txt", "r")
datastr = file.read()

for ch in range(len(datastr)-13):
    string=""
    for a in range(14):
        string+=datastr[ch+a]

    found=0
    for pos in range(14):
        if string.count(datastr[ch+pos]) == 1:
            found+=1

    if found == 14:
        print(string)
        print(ch+14)
        break