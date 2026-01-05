def effort(c,l,t):
	nue = pow(l,3)
	deno = (pow(c,3) * pow(t,4))
	K =  nue / deno 
	return K

def main():
	L = int(input("Enter the product size in KLOC: "))
	T_d = int(input("Enter the time takes by the system in months: "))
	print("Note - The State Technology Constants:\nPoor State = 2\nGood State = 8\nExcellent State = 11")
	C_k = int(input("Enter the state of technology constant: "))
	Effort = effort(C_k,L,T_d)
	print("Calculated Effort: ",Effort," PM")

if __name__ == '__main__':
	main() 				