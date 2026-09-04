# Basic math
print(10 + 3)   # 13 - Addition
print(10 - 3)   # 7  - Subtraction
print(10 * 3)   # 30 - Multiplication
print(10 / 3)   # 3.333... - Division (always gives float)

# Special operators
print(10 // 3)  # 3  - Floor division (rounds down)
print(10 % 3)   # 1  - Modulo (remainder)
print(10 ** 3)  # 1000 - Exponent (power)


#Python follows maths rules (PEMDAS)
result = 2 + 3 * 4      # 14 (not 20!)
result = (2 + 3) * 4    # 20 (parentheses first)

#Logical Operators

age = 20
has_license = True

#And
can_drive = age >= 18 and has_license
print(can_drive)



age = 20
has_license = False

can_drive = age >= 18 and has_license
print(can_drive)


#OR

age = 20
has_license = False
#age or license one statement have to be correct but here both is incorrect we checked it using or operator
can_drive = age >= 21 or has_license
print(can_drive)