""
#Simple program  checking the users name
""
# Read the input from the user as a single string and split it into a list of names based on commas
names = input("Enter your list of names (separated by commas): ").split(',')

# Remove duplicates by converting the list to a set and then back to a list
names = list(set(names))

# Sort the list of names in alphabetical order
names.sort()

# Print the sorted list without duplicates
print("Sorted list of names (without duplicates):", names)

#
length =len(names)
print("Number of unique name:",length)
