# 1 Day of Code Advent Calender

expenses = [""]

f = open("C:\\Users\jones\Desktop\Code\input.txt","r")
for x in f:
    expenses = f.read().splitlines()

f.close()
print("Number of elements are", len(expenses))

expenses_length = len(expenses)
for x in range(expenses_length):
    for y in range(expenses_length):
        for z in range(expenses_length):
            total = int(expenses[x])+int(expenses[y])+int(expenses[z])
            if (total == 2020):
                d1 = x
                d2 = y
                d3 = z
                print("Elements are", d1, ",", d2," and ",d3)
                print("Numbers are ", expenses[d1],",",expenses[d2]," and", expenses[d3])
                print("Total is ", int(expenses[d1])*int(expenses[d2])*int(expenses[d3]))      

print("End")