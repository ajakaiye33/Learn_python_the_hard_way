#understanding python symbols
# and
# is a logic and ,used to combined two statement that to be true both statement
# would need to be true

#example

orange = 8

water_melon = 8
fruit_juice = 10

if orange < fruit_juice and fruit_juice > water_melon:
    print("yes")

else:
    print("I'm afraid there will be no ffruit today")

#as
# it's often used to shorten the name of module in order to ease typing when
#refering to such module subsequently in the programme

import math as m

jut_kidding = 2
print(m.sqrt(jut_kidding))


#assert
#I have seen  it being used in programmes the requires you to pass the test. i think
#it common in programme that test your code against the right code

check = 2 + 8 **2 /4
#print(check)
assert check == 18

#break
# This is used to  break out of a loop to do certain thing. that is the loop
#did not run it full course

# i = 9
#
# while i < 0:
#     print(i)
#     i = i + 1
#     #if i == 7:
#         #break

for i in range(9):
    print(i)
    if i == 5:
        break
        print('it is five')
    continue

#lambda is a naless function 
g = lambda x: x **2
print(g(5))
