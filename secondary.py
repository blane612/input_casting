# author: <name here>
# date: <date here>

# -------------------- Section 4 -------------------- #

# Input | ASCII Art


# Objectives:
#   1. Diamond
#       a. Define a function that accept the parameters listed below.
#           Name   | Type(s)         | Description
#           symbol | Integer / Float | The symbol used to create the diamond.
#
#           The function should print the chevron seen in the output below using the symbol.
#       b. Prompt input from the user in the form of a single character, save it to a variable.
#       c. Call the function you defined to create the diamond, sending the character as an argument.
#
#       HINT: Start with a smaller diamond! Then make it bigger once you figure out the pattern.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> $
#
#           $
#          $$$
#         $$$$$
#        $$$$$$$
#       $$$$$$$$$
#      $$$$$$$$$$$ 
#     $$$$$$$$$$$$$
#      $$$$$$$$$$$
#       $$$$$$$$$
#        $$$$$$$
#         $$$$$
#          $$$
#           $
#
# ---- WRITE CODE BELOW ---- #
def dia(symbol):
  print(" " * 6 + symbol * 1)
  print(" " * 5 + symbol * 3)
  print(" " * 4 + symbol * 5)
  print(" " * 3 + symbol * 7)
  print(" " * 2 + symbol * 9)
  print(" " + symbol * 11)
  print(symbol * 13)
  print(" " + symbol * 11)
  print(" " * 2 + symbol * 9)
  print(" " * 3 + symbol * 7)
  print(" " * 4 + symbol * 5)
  print(" " * 5 + symbol * 3)
  print(" " * 6 + symbol * 1)
char = input('Enter character here: ')
print(type(char))
dia(char)

# A string is a datatype that represents text. We surround it with '' or ""
# type(object) --> Returns the data type that object

#   2. Framed Diamond
#       a. Define a function that accept the parameters listed below.
#           Name   | Type(s)         | Description
#           symbol1 | Integer / Float | The symbol used to create the diamond.
#           symbol2 | Integer / Float | The symbol used to create the frame.
#
#           The function should print the chevron seen in the output below using the symbol.
#       b. Prompt input from the user in the form of a single character, save it to a variable.
#       c. Prompt input from the user in the form of a single character again, and save it to a second variable.
#       d. Call the function you defined to create the framed diamond, sending the characters as arguments.
#
#       HINT: Start with a smaller diamond! Then make it bigger once you figure out the pattern.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> &
#   >> ~
#
#     ~~~~~~$~~~~~~
#     ~~~~~$$$~~~~~
#     ~~~~$$$$$~~~~
#     ~~~$$$$$$$~~~
#     ~~$$$$$$$$$~~
#     ~$$$$$$$$$$$~
#     $$$$$$$$$$$$$
#     ~$$$$$$$$$$$~
#     ~~$$$$$$$$$~~
#     ~~~$$$$$$$~~~
#     ~~~~$$$$$~~~~
#     ~~~~~$$$~~~~~
#     ~~~~~~$~~~~~~
#
# ---- WRITE CODE BELOW ---- #
#print(>> &)
#print(>> ~)

def dia(symbol):
  char2 = input('Enter character here: ')
  char3 = symbol

  print(char2 * 6 + symbol * 1 + char2 * 6)
  print(char2 * 5 + symbol * 3 + char2 * 5)
  print(char2 * 4 + symbol * 5 + char2 * 4)
  print(char2 * 3 + symbol * 7 + char2 * 3)
  print(char2 * 2 + symbol * 9 + char2 * 2)
  print(char2 * 1 + symbol * 11 + char2 * 1)
  print(symbol * 13)
  print(char2 * 1 + symbol * 11 + char2 * 1)
  print(char2 * 2 + symbol * 9 + char2 * 2)
  print(char2 * 3 + symbol * 7 + char2 * 3)
  print(char2 * 4 + symbol * 5 + char2 * 4)
  print(char2 * 5 + symbol * 3 + char2 * 5)
  print(char2 * 6 + symbol * 1 + char2 * 6)
dia(char)




