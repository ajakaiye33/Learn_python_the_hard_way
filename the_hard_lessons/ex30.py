people = 30
cars = 40
trucks = 15

# the blocks of code under the first if statement would be display if it passes
# the truthy condition or another if staement is that one passes the truthy condition
# otherwise do something else.
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

#display the blocks of code if the if staement is true or another if stement or otherwise
#do something else
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We can't decide.")

#displays the block of code if the statement is true, otherwise do something else
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")


#drills

"""
I guess elif is simply creating room for another condition to be tested which
would be entertained if the first if could not pass the truthy test. It's basically
another truth that could play its block of code when the first if conditon fails t
the truthy test

"""

if people > cars or cars < people:
    print("You can see me and read because one condition is true")
else:
    print("You are seeing me beacuse somethign has screwed up")
