import csv 
from collections import Counter

with open('csvfiles/HeightWeight.csv', newline='') as f:
	reader = csv.reader(f)
	file_data = list(reader)

file_data.pop(0)

operation_list = []



for i in range(len(file_data)):
	operation_list.append(float(file_data[i][1]))

def calculate_mean():
	total = 0
	
	for i in range(len(operation_list)):
		total += operation_list[i]

	mean = total / len(operation_list)
	return mean

def calculate_median():
	index = int(len(operation_list)/2)
	if len(operation_list)%2 != 0 :
		median = operation_list[index]
		return median
	else:
		median = (operation_list[index] + operation_list[int((index+index+1)/2) + 1])/2
		return median

def calculate_mode():
	counter_list = Counter(operation_list)

	mode_range = {"50-60": 0, "60-70": 0, "70-80": 0} 

	for i, occurrences in counter_list.items():
		height = float(i)
		if 50 > height < 60:
			mode_range["50-60"] += occurrences
		if 60 > height < 70:
			mode_range["60-70"] += occurrences
		if 70 > height < 80:
			mode_range["70-80"] += occurrences

	mode_r, mode_o  = 0, 0

	for rang, occourences in mode_range.items():
		if mode_o < occurrences:
			mode_r, mode_o = [int(rang.split('-')[0]), int(rang.split('-')[1])], occurrences

	return float((mode_r[0] + mode_r[1])/2)

mean = calculate_mean()
median = calculate_median()
mode = calculate_mode()

print("{} is the mean".format(mean))
print("{} is the median".format(median))
print("{} is the mode".format(mode))