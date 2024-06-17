def is_palindrome(num):
    # Convert the number to a string
    num_str = str(num)
    
    # Check if the string is equal to its reverse
    if num_str == num_str[::-1]:
        return True
    else:
        return False

# Prompt the user to enter a number
try:
    test_num = int(input("Enter an integer: "))
    
    
    if isinstance(test_num, int):
        if is_palindrome(test_num):
            print(f"{test_num} is a palindrome.")
        else:
            print(f"{test_num} is not a palindrome.")
except ValueError:
    print("Please enter a valid integer.")
