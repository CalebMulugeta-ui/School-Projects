import random
list = [[],[],[]]
value = 1

for i in range(0,3):
    for e in range(0,3):
        list[i].append(random.randint(1,25))

for row in list:
    for col in row:
        value = value * col
print(value)