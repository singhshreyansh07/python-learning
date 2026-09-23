
def add_number(a,b):
    print(a + b)

print_result = add_number(a=5, b=12)   #not using return here
#here if we just run print_result it will be empty.
#we can just print it not store it.


def add_no(a,b):
    return(a + b)  #here we using return to store the output

result = add_no(a=5, b=12)   #we storing output in result
#but here if we run result it will show stored value that's what return do.
result + 12  #now we can do other operations with it.


#another example

def calculate_area(width, height):
    area = width * height
    return area

room_area = calculate_area(15,16)
print(f"Room area is {room_area} sq ft")






def double(number):
    return number * 2

# Store in variable
result = double(5)

# Use in expressions
total = double(5) + double(3)  # 10 + 6 = 16

# Pass to other functions
print(double(10))  # 20

# Use in conditions
if double(7) > 13:
    print("Big number!")
else:
    print("Small number!")




#return multiple values from function

def calculation():
    numbers = [1,2,3,4,5]
    first_no = numbers[0]
    last_no = numbers[-1]
    return first_no, last_no

f, l = calculation()

print(f)
print(l)


#Return vs Print
def get_greeting_print(name):
    print(f"Hello, {name}!")  # Just displays

def get_greeting_return(name):
    return f"Hello, {name}!"  # Gives back value

# Can't use print version's output
message = get_greeting_print("Alice")  # Prints but returns None
print(message)  # None

# Can use return version's output
message = get_greeting_return("Alice")  # Returns the string
print(message.upper())  # HELLO, ALICE!