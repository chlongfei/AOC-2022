file = open("in.txt", "r")
score = 0

for ln in file:
    if ln[0] == "A":
        if ln[2] == "X":
            score+=(1+3)
        elif ln[2] == "Y":
            score+=(2+6)
        else:
            score+=(3+0)
    elif ln[0] == "B":
        if ln[2] == "X":
            score+=(1+0)
        elif ln[2] == "Y":
            score+=(2+3)
        else:
            score+=(3+6)
    else:
        if ln[2] == "X":
            score+=(1+6)
        elif ln[2] == "Y":
            score+=(2+0)
        else:
            score+=(3+3)

print ("Total Score: ", score)