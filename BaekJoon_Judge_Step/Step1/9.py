data = input()

a = int(data.split(' ')[0])
b = int(data.split(' ')[1])
c = int(data.split(' ')[2])

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)