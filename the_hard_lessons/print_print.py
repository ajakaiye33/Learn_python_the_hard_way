# the curly brances that would house variable or phrases
formatter = "{} {} {} {}"

#use to write figure/degit
print(formatter.format(1,2,3,4))
#used to write words in figure
print(formatter.format("one","two", "three", "four"))
#used to write boolean
print(formatter.format(True, False, False, True))
#used to print out the curly braces themselves
print(formatter.format(formatter, formatter, formatter, formatter))
#used to print well formatted structure of poems or songs or lyricsi
print(formatter.format(

     "Try your",
     "Own text here",
     "Maybe a poem",
     "Or a song about fear"
))
