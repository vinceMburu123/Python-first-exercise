# Function to determine the grade based on score
def determine_grade(score):
    if 70 <= score <= 100:
        return "A"
    elif 60 <= score <= 69:
        return "B"
    elif 50 <= score <= 59:
        return "C"
    elif 40 <= score <= 49:
        return "D"
    elif 0 <= score <= 39:
        return "Fail (Take a supplementary exam)"
    else:
        return "Invalid score"

# Get user input for the score
score = int(input("Enter the student's score: "))

# Determine the grade
grade = determine_grade(score)

# Print the grade
print(f"The grade is: {grade}")
