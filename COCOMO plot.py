import matplotlib.pyplot as plt

e1 = []
t1 = []
e2 = []
t2 = []
e3 = []
t3 = []

def calculate(table, model ,size):

	global e1,e2,e3,t1,t2,t3

	effort = 0
	time = 0

	effort = table[model][0]*pow(size, table[model][1])
	time = table[model][2]*pow(effort, table[model][3])

	if (model == 0):
		e1.append(effort)
		t1.append(time)
	elif (model == 1):
		e2.append(effort)
		t2.append(time)
	elif (model == 2):
		e3.append(effort)
		t3.append(time)

def cocomo(kloc):
	table = [[2.4,1.05,2.5,0.38],[3.0,1.12,2.5,0.35],[3.6,1.20,2.5,0.32]]
	calculate(table, 0, kloc)
	calculate(table, 1, kloc)
	calculate(table, 2, kloc)

def main():
	global e1,e2,e3,t1,t2,t3
	kloc = []
	for i in range(1,10000):
		kloc.append(i)
		cocomo(i)


	figure, axis = plt.subplots(1, 2)

	axis[0].plot(kloc,e1, label = 'Organic')
	axis[0].plot(kloc,e2, label = 'Semi-Detached')
	axis[0].plot(kloc,e3, label = 'Embedded')
	axis[0].set_xlabel("Size (kLOC)")
	axis[0].set_ylabel("Estimated Effort")
	axis[0].set_title("Size vs Effort")


	axis[1].plot(kloc,t1, label = 'Organic')
	axis[1].plot(kloc,t2, label = 'Semi-Detached')
	axis[1].plot(kloc,t3, label = 'Embedded')
	axis[1].set_xlabel("Size (kLOC)")
	axis[1].set_ylabel("Estimated Time (Month)")
	axis[1].set_title("Size vs Time")

	axis[0].legend()
	axis[1].legend()
	plt.show()

if __name__ == '__main__':
	main()
