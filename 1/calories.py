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

fat = np.max(elf)

print("Fattest elf calories: ", fat)