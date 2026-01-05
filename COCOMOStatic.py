def calculate(table, mode ,size):
	effort = 0
	time = 0
	person = 0
	model = 0

	if(size >= 1 and size <= 100):
		model = 0
	elif(size > 100 and size <= 500):
		model = 1
	elif(size > 500):
		model = 2
	
	print("Mode: ", mode[model])

	effort = table[model][0]*pow(size, table[model][1])
	
	time = table[model][2]*pow(effort, table[model][3])
	
	staff = effort/time

	print("Effort = {} Person-Month".format(round(effort)))
	print("Development Time = {} Months".format(round(time)))
	print("Average Staff Required = {} Persons".format(round(staff)))

def main():
	table = [[2.4,1.05,2.5,0.38],[3.0,1.12,2.5,0.35],[3.6,1.20,2.5,0.32]]
	mode = ["Organic","Semi-Detached","Embedded"]
	kloc = 180
	calculate(table, mode, kloc)

if __name__ == '__main__':
	main()
