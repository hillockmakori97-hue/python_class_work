print("Welcome to the wonderful world of Python!!!")
#question 2
print(""" Strathmore University exists to provide all-round quality education in an
atmosphere of freedom and responsibility, excellence in teaching, research
and scholarship, ethical and social development and service to society.""")
#question 3 
principle=600000
rate=8
time=6
interest=principle*rate*time/100
print(f"You deposited Sh {principle} and it accured an interest of Sh {interest}, your new amount is Sh {principle+interest}")
#quesion 4
year_birth=int(input("Enter Year Of Birth: "))
age=2026-year_birth
print(f"You are {age} years old")
#question 5
# prompt user to enter call duration in minutes 
minutes=int(input("Enter Call Duration(minute(s)): "))
# convert the minutes into seconds 
seconds=minutes*60
# Display output to the user using a fomatted string 
print(f"your call lasted {seconds} seconds and costs Sh {seconds*4}")
# Question 6
name=input("Enter First Name: ")
print(f"Hello, {name}, nice to meet you ")
# Question 7
length=int(input("Enter Length: "))
width=int(input("Enter Width: "))
if length==width:
    print("Shape is a square")
else:
    print("Shape is not a square")
# Question 8
salary=float(input("Input Salary: "))
yr_service=int(input("Input Years Of Service: "))
if not yr_service>5:
    print("Inelligble for Raise ")
else:
    salary_inc=1.05*salary
    bonus=salary_inc-salary
    print(f"Your have received a bonus of Sh {bonus}, Your net salary is sh{salary_inc}")
# question 9
number=int(input("Enter Number: "))
if number>=14 and number<=72 or number>103:
    print("Good")
else:
    print("Bad")
# question 10
score=int(input('Enter Scores: '))
if score>0 and score<=9:
    if score<=3:
        score=score*10
    elif score<=6:
        score=score*100
    else:
        score=score*1000
    print (f"Your have {score} bonus points")
else:
    print("Score out of range ")

# question 11
# Prompt for the cost of the two items
item1 = float(input("Enter the cost of the first item: $"))
item2 = float(input("Enter the cost of the second item: $"))

# Calculate total cost
total_cost = item1 + item2
print(f"Total cost: ${total_cost:.2f}")

# Prompt for the payment amount
payment = float(input("Enter your payment amount: $"))

# Check payment against total cost
if payment < total_cost:
    amount_owed = total_cost - payment
    print(f"Insufficient payment. You still owe ${amount_owed:.2f}.")
else:
    change = payment - total_cost
    print(f"Thank you for your payment! Your change is ${change:.2f}.")
# question 12

# Prompt the user for the wind speed
wind_speed = int(input("Enter the wind speed in mph: "))

# Determine hurricane category using the table thresholds
if wind_speed >= 155:
    print("This qualifies as a Category 5 hurricane.")
elif wind_speed >= 131:
    print("This qualifies as a Category 4 hurricane.")
elif wind_speed >= 111:
    print("This qualifies as a Category 3 hurricane.")
elif wind_speed >= 96:
    print("This qualifies as a Category 2 hurricane.")
elif wind_speed >= 74:
    print("This qualifies as a Category 1 hurricane.")
else:
    print("This wind speed does not qualify as a hurricane (must be at least 74 mph).")


