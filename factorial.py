def factorial(number):

    factorial=1

    for i in range(number):
        factorial*= i + 1




    return factorial

uInput = int(input("Please give me a number:"))

print(factorial(uInput))