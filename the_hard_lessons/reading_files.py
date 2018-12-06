# import the arguement variable from sys
from sys import argv
#assign script and filename to argv
script, filename = argv

#call open on the file and assign to variable txt
txt = open(filename)

#read the content of the file with the function "read()"
print(f"Here's your file {filename}:")
print(txt.read())
txt.close(s)
# #request from the user a name of s file to read
print("Type the filename again:")

file_again =input("> ")
#assigned the user's asnwer to to the file_again variable
txt_again = open(file_again)
#print the contents of the file
print(txt_again.read())
txt_again.close()
