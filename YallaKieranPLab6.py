#Kieran Yalla
#8/5/23
#Professor Phong Banh
#CMSC 135

numlist =[]
total = 0

for i in range(20):
    numinput = float(input(f"Enter number {i + 1} of 20: "))
    numlist.append(numinput)
    
for value in numlist:
    total += value

average = total / len(numlist)

lowest = min(numlist)
highest = max(numlist)

print("Low:",format(lowest,'.2f'))
print("High:", format(highest,'.2f'))
print("Total:", format(total,'.2f'))
print("Average:",format(average,'.2f'))
