
def morning():      #defining a function
    print("Good Morning!!")

morning()  #calling a function

#we use only lowercase in function no uppercase
#uppercase use for classes


def say_goodbye():
    print("Goodbye!")
    print("See you later!")

# Call it multiple times
say_goodbye()
say_goodbye()
say_goodbye()



#function with logic

def check_weather():
    temperature = 38
    if temperature >= 25:
        print("It's hot day")
    else:
        print("Nice weather my friend!!")

#calling the function
check_weather()