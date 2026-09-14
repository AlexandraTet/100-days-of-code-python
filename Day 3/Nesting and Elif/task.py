# maths_score = int(input("What is your maths score? "))
# english_score = int(input("What is your english score? "))
# if maths_score >= 90 and english_score >= 90:
#     print("You're good at everything")
# elif maths_score >= 90 and english_score < 90:
#     print("You're good at maths")
# elif english_score >= 90 and maths_score < 90:
#     print("You're good at english")
# else:
#     print("You need to study more")

# -----------------------------------------------------------------

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")

