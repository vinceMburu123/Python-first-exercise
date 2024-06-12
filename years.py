#Simple program of Bonus
salary=int(input("Enter Salary:"))
years_of_service=int(input("years_of_service:"))
if years_of_service >10:
    bonus =(salary*0.1)
    print(bonus)
elif years_of_service >=6 and years_of_service <=10:
    bonus= (salary*0.08)
    print(bonus)
elif years_of_service <6:
    bonus =(salary*0.05)
    print(bonus)
