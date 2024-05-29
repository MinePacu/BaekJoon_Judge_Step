data = input()

if int(data.split(' ')[0]) > int(data.split(' ')[1]):
	print(">")
elif int(data.split(' ')[0]) < int(data.split(' ')[1]):
	print("<")
else:
	print("==")