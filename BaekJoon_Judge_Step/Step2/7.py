data = input()

a = int(data.split(' ')[0])
b = int(data.split(' ')[1])
c = int(data.split(' ')[2])

result = 0
if a == b and b == c:
	result = 10000 + (a * 1000)
elif a == b or b == c or a == c:
	if a == b or a == c:
		result = 1000 + (a * 100)
	elif b == c:
		result = 1000 + (b * 100)
else:
	if a > b and a > c:
		result = a * 100
	elif b > a and b > c:
		result = b * 100
	elif c > a and c > b:
		result = c * 100

print(result)

