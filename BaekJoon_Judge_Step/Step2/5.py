time = input()

hour = int(time.split(' ')[0])
minute = int(time.split(' ')[1])

result_hour = hour
result_minute = minute 

if minute - 45 < 0:
	if result_hour - 1 < 0:
		result_hour = 23
	else:
		result_hour -= 1
	result_minute = 60 + (minute - 45)

else:
	result_minute = minute - 45

print(f"{result_hour} {result_minute}")