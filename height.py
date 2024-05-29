"Code for checking height of the students"
""
Author :Vincent 

""
# Get input for three students
name1 = input("Enter the name of student 1: ")
height1 = int(input(f"Enter the height of {name1} in cm: "))

name2 = input("Enter the name of student 2: ")
height2 = int(input(f"Enter the height of {name2} in cm: "))

name3 = input("Enter the name of student 3: ")
height3 = int(input(f"Enter the height of {name3} in cm: "))


students = [
    (name1, height1),
    (name2, height2),
    (name3, height3)
]

# Print the heights of all students
for student in students:
    print(f"{student[0]}: {student[1]}cm")

# Determine the tallest student
if height1 > height2 and height1 > height3:
    tallest_student = (name1, height1)
elif height2 > height1 and height2 > height3:
    tallest_student = (name2, height2)
else:
    tallest_student = (name3, height3)

# Print the tallest student
print(f"{tallest_student[0]} is the tallest")
