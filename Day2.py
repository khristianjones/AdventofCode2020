#Day 2 of Code Advent Calender
import re
passwords = [""]

f = open("C:\\Users\jones\Desktop\Code\input2.txt","r")
for x in f:
    passwords = f.read().splitlines()

f.close()
print("Number of elements are", len(passwords))

count = 0

for x in range(len(passwords)):
    input_line = passwords[x].split() #0 num of occurances, 1 character, 2 string
    z = 0
    limits = input_line[0].split('-')
    lowerLim = int(limits[0])
    upperLim = int(limits[1])
    for i in input_line[2]:
        if (i == input_line[1][0]):
            z = z +1 
    if (z >= lowerLim and z <= upperLim):
        count = count + 1 

print("The number of acceptable passwords is ", count)

