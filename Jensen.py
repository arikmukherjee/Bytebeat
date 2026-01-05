import matplotlib.pyplot as plt

def jensen(cte, td, k):
        return (cte * td * pow(k, 1/2))

def main():
	cte = float(input("Enter the effective technology constant: "))
	td = float(input("Enter the time to develop the software: "))
	k  = float(input("Enter the effort needed to develop the software: "))
	
	print("The estimated product size (L): {} KLOC".format(jensen(cte, td, k)))
	
	y = [round (jensen (cte, time, k), 5) for time in range(0, 3*int(td))]
	plt.plot(y, label="Product Size per unit time")
	plt.legend(loc= "upper right")
	plt.xlabel("time")
	plt.ylabel("L(Product size)")
	plt.show()

if __name__ == "__main__":
	main()
