menuList = []

def showBill():
    total = 0
    print("---PP Restaurant---")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        total += int(menuList[number][1])
    print("Total :",total,"THB.")

while True:
    menuName = input("Enter The Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price:")
        menuList.append([menuName,menuPrice])
print(menuList)
showBill()