# Pattern 1: Import the whole module
import math
# Now use: math.sqrt(16)
math.sqrt(49)

# Pattern 2: Import specific items from a module
from math import sqrt, pi
# Now use: sqrt(16)
sqrt(16)  #no need to do math.sqrt here bcz we didn't imported math
#we just imported sqrt and pi from maths.




import random

number = random.randint(1, 9)  #choosing random no from 1 to 9
#we can create gamble or guess game using it.

fruit = random.choice(["apple","banana","mango","orange","watermelon"])






# Date and time
import datetime
today = datetime.date.today()
print(today)  #2026-09-23



#operating system
import os

current_dir = os.getcwd()
print(current_dir)