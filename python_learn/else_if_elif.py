temperature = 31

if temperature > 30:
    print("Very Hot!!")
if temperature > 25:
    print("It's Hot")
else:
    print("Nice weather")


#In the above case we using two if so the output we r getting is:
#Very Hot!!
#It's Hot


temperature = 32

if temperature > 30:
    print("Very Hot!!")
elif temperature > 25:
    print("It's Hot")
else:
    print("Nice weather")


#Now here we r using elif instead of if so the output now is:
#Very Hot!!


#More practice

score = 65

if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Good")
elif score >= 70:
    print("Trillionaire & Best in the World")
else:
    print("Work Hard")




#Combine and code use and condition

age = 8
has_licensed = True
time = 18 - age

if age >= 18 and has_licensed:
    print("Eligible for driving")
elif age <= 10:
    print("Gonna beat your ass kid")
else:
    print(f"Lil bro wait for {time} year")


weekend = "Saturday"
holiday = "Tuesday"
# At least one must be True
if weekend or holiday:
    print("No work today!")

