#Calculate Gross pay /Just for insert values
"""
Code to calculate gross pay
Author:Vincent
Date:18th May 2024
"""
hours =35
rate_per_hour=2.75

gross_pay= hours * rate_per_hour

print(gross_pay)

print(type(hours))
print(type(rate_per_hour))
print(type(gross_pay))

#With Prompting inputs
#Calculate gross pay
"""
Code to calculate gross pay

"""
hours = int(input("Enter the number of hours worked:")) 
rate_per_hour=int(input("Enter the rate_per_hour :")) 

gross_pay= hours * rate_per_hour

print("Gross Pay:", gross_pay)
print("Type of hours:", hours)
print("Type of rate_per_hour:", rate_per_hour)
print("Type of gross_pay:", gross_pay)
