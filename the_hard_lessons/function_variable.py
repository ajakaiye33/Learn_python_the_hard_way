
def cheeese_and_crackers(cheese_count, box_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {box_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")


# here the arguement were applied directly to the function
print("We can just give the function numbers directly:")

cheeese_and_crackers(20,30)




#here the arguements were assigned to variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50



cheeese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
# here the arguement were applied with an operation
cheeese_and_crackers(10 + 20, 5 + 6)

# here the arguement weren't only assign to variables but made to carry operation
print("And we can combine the two, variable and math:")

cheeese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
