file = open("in.txt", "r")

full=0

for ln in file:
    pair=ln.split(",")

    p1=pair[0].split("-")
    p2=pair[1].split("-")

    if int(p1[0]) <= int(p2[0]) and int(p1[1]) >= int(p2[1]):
        full+=1
    elif int(p2[0]) <= int(p1[0]) and int(p2[1]) >= int(p1[1]):
        full+=1

print(full)