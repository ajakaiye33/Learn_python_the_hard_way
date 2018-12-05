from sys import argv

# script, user_name = argv
#
# prompt = '> '
#
#
# print(f"Hi {user_name}, I'm the {script} script.")
# print("I'd like to ask you a few questions.")
# print(f"Do you like me {user_name}?")
# likes = input(prompt)
#
# print(f"Where do you live {user_name}? ")
# lives = input(prompt)
#
# print(f"What kind of computer do you have?")
#
# computer = input(prompt)
#
# print(f"""
# Alright, so you said {likes} about liking me.
# You live in {lives}. Not sure where that is.
# And you have a {computer} computer. Nice.
# """)

# Drills

script, age, carrer = argv

prompt = ">>> "

print(f" Hey I'm {script} and I can see you are {age} old that dream of becoming a {carrer}")

print(f" Before we get into talking about how to thrive as {carrer}, I have a couple of questions ")

print(" Did you like Calculus in College?")

calcu = input(prompt)

print("Did like Algebra in High School?")
alg = input(prompt)

print("Did like Statistics in college?")

sts = input(prompt)


print(f"""
Ok, so you are {age} years old that would like to carve a career in {carrer} And
you said {calcu} to having some foundation in calculus and {alg} to studying some
Algebra  and {sts} to practicing Statistics. Then I'm convinced {carrer} jobs would
look for you
""")
