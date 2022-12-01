import numpy as np

inputFile = open("in.txt", "r")

elf = []

sumCal = 0
for ln in inputFile:
    if ln == '\n':
        elf.append(sumCal)
        sumCal = 0
    else:
        sumCal += int(ln)

sumCalTop3 = 0
for ef in range(3):
    fat = np.max(elf)
    sumCalTop3 += fat
    elf.remove(fat)

print("Sum of calories of top 3 fattest elves: ", sumCalTop3)