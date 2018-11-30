tabby_cat = "\tI'm tabbed in."

persian_cat = "I'm split\non a line"

backslash_cat = "I'm \\ a \\ cat."


fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)

print(persian_cat)

print(backslash_cat)

print(fat_cat)


knowl = '''
I didn't know:
\tthat there \aare
\tmore escape \bcharacter
\tthan \n it's really eye-opening for me
'''

print(knowl)


syr = 'Combining escape character and string {} {}'.format(persian_cat,knowl)

print(syr)
