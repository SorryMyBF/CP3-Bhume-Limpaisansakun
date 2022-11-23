def plus(a, b):
    c = a + b
    print(a, "+", b, "=", c)


def minus(a, b):
    c = a - b
    print(a, "-", b, "=", c)


def multiply(a, b):
    c = a * b
    print(a, "*", b, "=", c)


def divide(a, b):
    c = a / b
    print(a, "/", b, "=", c)


a = int(input("FirstNumber:"))
b = int(input("SecondNumber:"))

print("1:+   2:-   3:*   4:%")
select = int(input("Please Enter The Option:"))
if select == 1:
    plus(a, b)
elif select == 2:
    minus(a, b)
elif select == 3:
    multiply(a, b)
elif select == 4:
    divide(a, b)
else:
    print("Error, please try again")
