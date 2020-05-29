import sys, csv, os
import matplotlib
import matplotlib.pyplot as plt

def read_file(file_name, x, y):
	val = 0
	with open(file_name) as file:
		c = 0
		reader = csv.reader(file)

		file = open(file_name)
		numlines = len(file.readlines())

		next(reader)
		for row in reader:
			num = find_ip(row)

			if(num != 0):
				val += num 
			if "M" in row[8]:
				y_v = float(row[8][0:-1])
			else:
				y_v = float(row[8]) / (1024 * 1024)
			y.append(y_v)
			
			x.append(c)
			
			c += 1
			
	return val


def find_ip(s):
	if(ip in s[5]):
		if "M" in s[8]:
			return(float(s[8][0:-1]))
		else:
			return(float(s[8]) / (1024 * 1024))
	else:
		return 0


os.system('cls')

file_name = sys.argv[1] 
ip = sys.argv[2]
price = float(sys.argv[3])

x = []
y = []

traf = read_file(file_name, x, y)

print("Total price for IP: " + ip + " = " + str(traf * price))
plt.plot(x, y)

plt.show()