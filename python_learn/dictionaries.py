person = {
    "name": "Shreyansh",
    "city": "New York",
    "age" : "18",
    "networth": "459$ Billion",
    "Date": "6 August 2030"
}

person["name"]       #Dictionaries we use like this
"""
output is {'name': 'Shreyansh',
 'city': 'New York',
 'age': '18',
 'networth': '459$ Billion',
 'Date': '6 August 2030'}
"""
#now to change any thing we can do
person["city"] = "Jaunpur"
"""
now output is {'name': 'Shreyansh',
 'city': 'Jaunpur',
 'age': '18',
 'networth': '459$ Billion',
 'Date': '6 August 2030'}
"""



#lets add something more in our dictionaries
person["license"] = True
person["car"] = "Mercedes AMG G63"

"""
output is now   {'name': 'Shreyansh',
 'city': 'Jaunpur',
 'age': '18',
 'networth': '459$ Billion',
 'Date': '6 August 2030',
 'license': True,
 'car': 'Mercedes AMG G63'}
"""

#to delete any thing we do

del person["license"]




#dictionaries methods
person = {"name": "Alice", "age": 30, "city": "New York"}
person.keys()
person.values()

if "name" in person:
    print("Name found")
else: 
     print("Not found")