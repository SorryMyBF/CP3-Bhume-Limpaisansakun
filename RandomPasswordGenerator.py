import random

print("นี่คือเครื่องสุ่มพาสเวิร์ด")
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#&*.,/()_+-='
number = input("จำนวนที่คุณต้องการ:")
number = int(number)
lenght = input("จำนวนตัวอักษรที่คุณต้องการ:")
lenght = int(lenght)

print("นี่คือพาสเวิร์ดของคุณ:")

for pwd in range(number):
    passwords = ""
    for c in range(lenght):
        passwords += random.choice(chars)
    print(passwords)
