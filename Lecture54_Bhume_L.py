username = "admin"
password = "1234"

def login():
	usernameInput = input("Enter Username : ")
	passwordInput = input("Enter Password : ")
	if usernameInput == username and passwordInput == password:
		print("Login Success")
		showMenu()
	else:
		print("Login Failed Please Try again")
		login()

def showMenu():
	print("---Pooh Furniture---")
	print("1.Vat Calculator")
	print("2.Total Price Calculator")
	userSelect = int(input("Enter the Menu or End This Process (1 2 or 0) : "))
	return menutSelect(userSelect)
def menutSelect(userSelect):
	while userSelect !=0:
		if userSelect == 1:
			totalPrice = float(input("Enter Price[THB] : "))
			return vatCalculate(totalPrice)
		elif userSelect == 2:
			return priceCalculate()
		else:
			print("Please Try again")
			showMenu()
	else:
		print("Done")
		exit()

def vatCalculate(totalPrice):
	vat = 7/100
	print("Vat", "{:.0%}".format(vat), ": ", "{:,.2f}".format(totalPrice*vat))
	result = totalPrice*(1+vat)
	print("Total Vat Incl. : ", "{:,.2f}".format(result))
	return result, showMenu()


def priceCalculate():
	countItem = int(input("Number of Item? : "))
	totalPrice = 0
	for i in range(1, countItem+1):
		x = float(input("Item No." + str(i) + " Price : "))
		totalPrice += x
	print("Total : ", "{:,.2f}".format(totalPrice))
	return vatCalculate(totalPrice), showMenu()

login()