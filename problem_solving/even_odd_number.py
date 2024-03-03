# numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# even_numbers = []
# odd_numbers = []
# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
#     else:
#         odd_numbers.append(number)
# print("Even numbers: ", even_numbers)

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
