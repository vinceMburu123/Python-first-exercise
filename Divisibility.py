
""
# Code for Divisibility
""
#Code for divisibility 5,7,11
""

number = int(input("Enter a number: "))

# to track if the number is divisible by any of the divisors
divisible = False

# Check divisibility
if number % 5 == 0:
    print(f"{number} is divisible by 5")
    divisible = True
elif number % 7 == 0:
    print(f"{number} is divisible by 7")
    divisible = True
elif number % 11 == 0:
    print(f"{number} is divisible by 11")
    divisible = True

# Check if the number is even
if number % 2 == 0:
    print(f"{number} is even")
    divisible = True

# If the number is not divisible by 5, 7, 11, and is not even
if not divisible:
    print(f"{number} is not divisible by 5, 7, 11, and is not even")

