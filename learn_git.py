print("This is from git main ... ")
print("This is from Main ... ")

# Regular Expressions

# [abc]       # a,b or c
# [^abc]      # any character except a,b,c
# [a - z]     # a to z
# [A - Z]     # A to Z
# [a - z A - Z]       # a to z, A to Z
# [0 - 9]     # 0 to 9


# Quantifiers

# [ ]?      # occurs 0 or 1 times
# [ ]+      # occurs 1 or more times
# [ ]*      # occurs 0 or more times
# [ ]{n}      # occurs n times
# [ ]{n, }      # occurs n or more times
# [ ]{y, z}      # occurs atleast y times but less than x times


# Regex Special Sequences

# \d    [0-9]
# \D    [^0-9]
# \w    [a-z A-Z 0-9]
# \W    [^a-z A-Z 0-9]
# and many more


import re 

x = "Regex means Regular Expression. 1 $ The re module offErs a set of functions that allows us to search a string + $ 2 for a match"

searching = re.search(r"^Regex.*functions", x)      # Simple example of ReGex
print(searching)