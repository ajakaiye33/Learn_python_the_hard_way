

types_of_people = 10
# the variable, types_of_people is place within the curly bracket in f string
x = f"There are {types_of_people} types of people."
# double quote is used to assign "binary" to the variable binary
binary = "binary"
# use double quote if you need to use quotes inside a quotes
do_not = "don't"
#f string is used to assign the respective variable in the sentence assigned to y
y = f"Those who know {binary} and those who {do_not}."

print(x)

print(y)
#f string splace directly inside the print function
print(f"I said: {x}")
# f string is used to place the variable y as a quoted phrase
print(f"I also said: '{y}'")


hilarious = False
#
joke_evaluation = "Isn't that joke so funny?! {}"
# f string and format are used in one statement, awesome!
print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."

e = "a string with a right side."
#variable are concatenated!
print(w + e)
