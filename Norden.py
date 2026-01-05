import matplotlib.pyplot as plt

def norden(k, td, t):
	a = pow(t, 2)
	b = 2 * (pow(td, 2))
	c = pow(2.7182, (-a/b))
	effort = (k/pow(td, 2)) * t * c
	return effort

def main():
	k = float(input("Enter the area under the curve(k): "))
	td = float(input("Enter the time at which the curve attains maximum value(td): "))
	t = float(input("Enter the effort time(t): "))
	
	print("\n The effort(E) required at time t is: \nE =",norden(k,td,t),"PM")

	y = [round (norden (k, td, time), 5) for time in range(0,3*int(td))]
	plt.plot(y, label="Effort per unit time")
	plt.vlines( 
        x=td, 
        ymin=0, 
        ymax=round(norden (k, td, td), 5), 
		color = "black",
        linestyle="dashed",
        label="td"
    )
	plt.legend(loc= "upper right")
	plt.xlabel("time")
	plt.ylabel("Effort per unit time")
	plt.show()

if __name__ == "__main__":
	main()
