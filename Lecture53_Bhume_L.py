total_p = int(input("Enter your total price:"))

def vat_calculation(total_p):
    result = total_p+(total_p*(7/100))
    return result

result = vat_calculation(total_p)
print("The Total Price And VAT",result," THB")