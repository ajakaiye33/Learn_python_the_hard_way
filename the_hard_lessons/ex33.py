# i = 0
# numbers = []
# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)
#
#
#
#     i = i + 1
#
#     print("Number now: ", numbers)
#     print(f"At the bottom i is {i}")
#
# print("The numbers: ")
#
# for num in numbers:
#     print(num)




#drills

def while_looper(max,incre):
    i = 0
    numbers = []
    while i < max:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + incre

        print("Number now: ", numbers)
        print(f"At the bottom i is {i}")

    for num in numbers:
        print(num)

see_inside = while_looper(10, 1)

print(see_inside)


def for_looper(max):
    numbers = []
    #print(f"what is {i}")
    for i in range(max):
        print(f"At the top i is {i}")
        numbers.append(i)
        print("number now:", numbers)
        print(f"at the bottom i is {i}")
        print(i)


print(for_looper(8))
