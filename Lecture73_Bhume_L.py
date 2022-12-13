systemMenu = {"Spaghetti": 150, "German Sausage": 180, "Spaghetti Meatball": 200, "Egg Fried Rice": 50}
menuList = []

def showBill():
    total = 0
    print("---PP Restaurant---")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        total += int(menuList[number][1])
    print("Total :",total,"THB.")

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

print(menuList)
showBill()