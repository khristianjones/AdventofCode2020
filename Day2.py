#Day 2 of Code Advent Calender
passwords = [""]

def part_a():
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

def part_b():
    count = 0
    for x in range(len(passwords)):
        input_line = passwords[x].split() #0 num of occurances, 1 character, 2 string
        z = 0
        limits = input_line[0].split('-')
        lowerLim = int(limits[0])
        upperLim = int(limits[1])
        character = input_line[1][0]
        if (character == input_line[2][lowerLim-1]):
            z = z + 1 
        if (character == input_line[2][upperLim-1]):
            z = z + 1
        if (z == 1):    
            count = count + 1

    print("The number of acceptable passwords is ", count)


f = open("input2.txt","r")
for x in f:
    passwords = f.read().splitlines()

f.close()
print("Number of elements are", len(passwords))
part_a()
part_b()

