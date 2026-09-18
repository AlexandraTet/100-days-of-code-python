# for number in range(1, 10): # not including 10
# for number in range(1, 11, 3): # step size of 3, result: 1, 4, 7, 10
#     print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)