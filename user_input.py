#Mad libs
adjective1 = input("Enter adjective: ")
noun = input("Enter noun: ")
adjective2 = input("Enter adjective: ")
verb = input("Enter verb: ")
adjective3 = input("Enter adjective: ")

print(f"Today I went to a {adjective1} zoo. ")
print(f"In an exhibit, I saw {noun}")
print(f"{noun} was {adjective2} and {verb}ing")
print(f"I was {adjective3}")

#Area calc
length = float(input("Enter the length of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))

area = length * width
print(f"The area is: {area}cm^2")

#shopping cart
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${round(total, 2)}")