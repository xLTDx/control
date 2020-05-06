import sys, csv, os
from datetime import datetime
from datetime import timedelta 

def open_file(file_name):
	ar = []
	title = []
	with open(file_name) as file:
		reader = csv.reader(file)
		for row in reader:
			title.append(row)
			break
		for row in reader:
			ar.append(row)
		title[0].append("cost")
	file.close()
	return ar, title[0]

def calc(ar):
	for i in range(len(ar)):
		result = 0
		get_date_time = ar[i][0]
		get_date = get_date_time.split()[0]

		call_date_time = datetime.strptime(get_date_time, '%Y-%m-%d %H:%M:%S')
		night_date_time = datetime.strptime(get_date + " 00:30:00", '%Y-%m-%d %H:%M:%S')

		if call_date_time < night_date_time:	
			if call_date_time + timedelta(minutes=float(ar[i][3])) < night_date_time:
				result = float(ar[i][3]) * 4
			else:
				before_night = (night_date_time - call_date_time).total_seconds()
				after_night = float(ar[i][3]) * 60 - before_night	
				result = (before_night / 60 * 4) + (after_night / 60 * 2)					

		if call_date_time >= night_date_time:
			result = float(ar[i][3]) * 2
	
		if ar[i][4] > 5:
			result += (float(ar[i][4]) - 5) * 1.5

		res.append([result])

	return res

def display(ar, title, res):
	ar.insert(0, title)
	
	for i in range(0, len(ar) - 1):
		ar[i+1].append(res[i][0])

	for j in range(0, len(ar)):
		row = []
		for i in range(0, len(ar[0])):
			row.append(ar[j][i])

		print("%20s%14s%12s%14s%11s%8s" % tuple(row))

def sum(ar):
	total = 0
	for i in ar:
		total += i[0]
	return total

os.system('cls')

file_name = sys.argv[1] 

calls = []
res = []

f = open_file(file_name)

calls = f[0]
title = f[1]
res = calc(calls)

display(calls, title, res)

print '\nTotal: ' + str(sum(res))






