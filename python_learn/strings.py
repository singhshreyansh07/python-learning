string = "My name is Shreyansh Singh"
#single line string

my_long_string = """
My name is Shreyansh Singh.
I don't ever give up.
I always attract what i want.
"""

first_name = "Shreyansh"
last_name = "Singh"

#printed full name but without space.
#full_name = first_name + last_name

#printing with space. easy concept
full_name = first_name + " " + last_name



#Lets play
dash = "-" * 10000

len(first_name + last_name)



#f string
#first without f string
name = "Shreyansh"

string = "Hi there, my name is {name}"

#output is this = 'Hi there, my name is {name}'

#now let's do it with f string
name = "Shreyansh"

string = f"Hi there, my name is {name}"

#output = 'Hi there, my name is Shreyansh'