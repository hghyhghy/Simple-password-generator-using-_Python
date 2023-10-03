# imporrting string module

import string

# importing  random module

import random


# printing lower case characters

s1 = string.ascii_lowercase

print(s1)

# printing upper case characters


s2 = string.ascii_uppercase

print(s2)


# printing the digits

s3 = string.digits

print(s3)

# printing the punctuation

s4 = string.punctuation

print(s4)

# taking the inpu from the user


plen = int(input("Enter the length of the password\n"))

# creating an empty list

s = []

s.extend(list(s1))

s.extend(list(s2))

s.extend(list(s3))

s.extend(list(s4))

# printing the etended  list


print(s)

# shuffling the elements from the extended list s

random.shuffle(s)

print(s)

# now we have to extraxt five elements from the list

print("Your password is :")

print("".join(s[0:plen]))

# the join function concatenate the all 5 five values without any space  / empty delimiter

# by using random .sample

print("Your password is :")

print("".join(random.sample(s, plen)))
