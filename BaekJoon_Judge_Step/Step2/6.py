import math

time = input()
time_gap = int(input())

hour = int(time.split(' ')[0])
minute = int(time.split(' ')[1])

result_hour = hour
result_minute = minute 

if (minute + time_gap) / 60 >= 1:
	if result_hour + ((minute + time_gap) / 60) >= 24:
		result_hour = math.trunc(24 - (result_hour + ((minute + time_gap) / 60))) * -1
	else:
		result_hour += math.trunc((minute + time_gap) / 60)
	result_minute = ((minute + time_gap) % 60)

else:
	result_minute = minute + time_gap

print(f"{result_hour} {result_minute}")