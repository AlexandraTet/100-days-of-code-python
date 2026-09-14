print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You have chosen an invalid size.")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

# if size == "S":
#     print("Your pizza is $15")
#     if pepperoni == "Y":
#         print("Your pizza is $17")
#     else:
#         print("Your pizza is $15")
#     if extra_cheese == "Y":
#         print("Your pizza is $16")
#     else:
#         print("Your pizza is $15")
#     if pepperoni == "Y" and extra_cheese == "Y":
#         print("Your pizza is $18")
# elif size == "M":
#     print("Your pizza is $20")
#     if pepperoni == "Y":
#         print("Your pizza is $23")
#     else:
#         print("Your pizza is $20")
#     if extra_cheese == "Y":
#         print("Your pizza is $21")
#     else:
#         print("Your pizza is $20")
#     if pepperoni == "Y" and extra_cheese == "Y":
#         print("Your pizza is $24")
# elif size == "L":
#     print("Your pizza is $25")
#     if pepperoni == "Y":
#         print("Your pizza is $28")
#     else:
#         print("Your pizza is $20")
#     if extra_cheese == "Y":
#         print("Your pizza is $26")
#     else:
#         print("Your pizza is $20")
#     if pepperoni == "Y" and extra_cheese == "Y":
#         print("Your pizza is $29")
# else:
#     print("You have chosen an invalid size.")

