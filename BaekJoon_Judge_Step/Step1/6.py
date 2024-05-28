import math

data = input()
print(int(data.split(' ')[0]) + int(data.split(' ')[1]))
print(int(data.split(' ')[0]) - int(data.split(' ')[1]))
print(int(data.split(' ')[0]) * int(data.split(' ')[1]))
print(math.trunc(int(data.split(' ')[0]) / int(data.split(' ')[1])))
print(int(data.split(' ')[0]) % int(data.split(' ')[1]))