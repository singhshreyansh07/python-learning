def greet():    #without parameters
    print("Hi,Shreyansh")

greet()


#With Parameters
def greet(name, last_name):
    print(f"Hi {name} {last_name}")


greet("Shreyansh", "Singh")
greet(name="Shaurya")
greet(name="Mylove")




def calculator_tax(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")

calculator_tax(100,0.02,10)