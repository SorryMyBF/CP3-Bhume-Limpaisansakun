class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Add to", self.name, self.lastname, "'s", "cart")

customer1 = Customer()
customer1.name = "Bhume"
customer1.lastname = "Limpaisansakun"
customer1.age = 18
customer1.addCart()

customer2 = Customer()
customer2.name = "Nutchapon"
customer2.lastname = "Chunjaren"
customer2.age = 19
customer2.addCart()

customer3 = Customer()
customer3.name = "Prashant"
customer3.lastname = "Pandee"
customer3.age = 18
customer3.addCart()

customer4 = Customer()
customer4.name = "Teeravut"
customer4.lastname = "Jareenkrung"
customer4.age = 17
customer4.addCart()

customer5 = Customer()
customer5.name = "Sarun"
customer5.lastname = "Sono"
customer5.age = 21
customer5.addCart()