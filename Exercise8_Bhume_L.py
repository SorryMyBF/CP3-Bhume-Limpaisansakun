username = "Nimda"
password = "4321"

productList = ["Chair", "Table", "Lather Sofa", "Shelf"]
productPrice = [800, 3000, 6000, 4500]
itemPriceList = []
itemList = []
productSelect = 0
productQty = 0
vat = 7/100
totalProductPrice = 0

def endLineText():
    print("---------------")

def showProductList():
    print("1 : ", productList[1], "/ Price[THB] ", "{0:,.2f}".format(productPrice[1]))
    print("2 : ", productList[2], "/ Price[THB] ", "{0:,.2f}".format(productPrice[2]))
    print("3 : ", productList[3], "/ Price[THB] ", "{0:,.2f}".format(productPrice[3]))
    print("4 : ", productList[4], "/ Price[THB] ", "{0:,.2f}".format(productPrice[4]))

def showProduceName():
    print("You'd like : ", productList[productSelect], "/ Price : ", "{0:,.2f}".format(productPrice[productSelect]),
          "THB")

def showProducePrice():
    totalProductPrice = productPrice[productSelect]*productQty
    print("You'd like : ", productList[productSelect], "/ Price : ", "{0:,.2f}".format(productPrice[productSelect]),
          "/ Total Price", "{0:,.2f}".format(totalProductPrice), "THB")
    itemPriceList.append(totalProductPrice)
    itemList.append(productList[productSelect])

usernameInput = input("Username : ")
passwordInput = input("Password : ")

if username == usernameInput and password == passwordInput:
    print("---Login Success---")
    print("----Welcome CTS Furniture----")
    endLineText()
    showProductList()
    productSelect = int(input("Which product are you looking for ? >>> "))
    showProduceName()
    productQty = int(input("How much you get this? >>> "))
    showProducePrice()
    productSelect = int(input("Want anything Else? (or 0) >>> "))
    while productSelect != 0:
        showProduceName()
        productQty = int(input("How much you get this? >>> "))
        showProducePrice()
        productSelect = int(input("Want anything Else? (or 0) >>> "))
    endLineText()
    print(itemList)
    print(itemPriceList)
    totalPrice = sum(itemPriceList)
    totalPriceExclVat = (totalPrice/(1+vat))
    endLineText()
    print("Total (Vat Excl.) : ", "{0:,.2f}".format(totalPriceExclVat))
    print("Vat", "{0:.0%}".format(vat), ":", "{0:,.2f}".format(totalPriceExclVat*vat))
    print("Total [THB] : ", "{:,}".format(totalPrice))
    endLineText()
    print("Thank you and Have a nice day ^^")
    print("----CTS Furniture----")
else:
    print("Username or Password Incorrect")