import random

# random_number = random.randint(1, 10)
# print(random_number)

# # random_number_0_to_1 = random.random() # random.random() generates a number between 0 and 1 (including 0, but not including 1)
# random_number_0_to_1 = random.random() * 10 # by multiplying it by 10, we get a number between 0 and 10 (including 0, not including 10)
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10) # random.uniform(1, 10) generates a number between 1 and 10 (including 1 and 10)
# print(random_float)

# print(random.choice(["Heads", "Tails"])) # random.choice([a, b]) generates a random choice from the list

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")