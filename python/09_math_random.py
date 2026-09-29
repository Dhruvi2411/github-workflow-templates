import math
import random

# help(math)
val = 4.5
print(math.ceil(val))
print(math.floor(val))
print(round(val))
print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)

### NUMPY ####
print(math.log(100,10))
print(math.log(math.e))
print(math.radians(180))

### RANDOM ###
print(random.randint(1,10))
# random.seed(120)
print(random.randint(1,100))
# print(random.randint(1,100))
# print(random.randint(1,100))
# print(random.randint(1,100))
# print(random.randint(1,100))

########
mylist = list(range(0,10))
print(mylist)
print(random.choice(mylist))

print(random.uniform(a=10,b=100))
