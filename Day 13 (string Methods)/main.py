a = "!! Harry !! Harry"
# strings are immutable
print(len(a))
# upper() => convert string to uppercase(capital)
print(a.upper()) 
# lower() => convert string to lowercase(small)
print(a.lower())

# strip("!") => remove all the ! from endling of the string
print(a.rstrip("!"))
# replace() => replace all the string with the defined new string
print(a.replace("Harry" , "jon"))
# split() => convert the string into list behalf of space or special character
print(a.split(" "))

# capitalize() => convert first character of string into uppercase
blogHeading = "introduction to jS"
print(blogHeading.capitalize())

str1 = "Welcome to the console!!!"
print(str1)
print(len(str1))
print((str1.center(50)))

# count() => gives the count of how many times the character or string occur in a given string
print(a.count("Harry"))

print(str1.endswith("!"))
print(str1.endswith("to",4,10))

# find() => gives index of first occurs of that word.It gives -1 value if the word is not present.

str1 = "He's name is Dan. He is an honest man"
print(str1.find("is"))

# index() => It is similar to find() methoud but it gives error if word is not present.
# print(str1.index("ishh"))

#isalnum() => it is a method that check whether a string is alphanumeric or not.(true or false)
#alphanumeric => A-Z,a-z,0-9

str1 = "welcomeToTheConsole09"
print(str1.isalnum())

# isalpha() => it cheks whether a string consist of A-Z,a-z
print(str1.isalpha())

# islower() => Returns true if the string is in lower case.

# isupper() => Returns true if the string is in upper case.

# isprintable() => Returns true if the string consist of pritable characters . non-pritable characters are \n

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())

# isspace() => it returns true if there are only spaces in a string.
str1 = "   "
print(str1.isspace())

# istitle() => returns true only if the first letter of each word of the string is capitalized

# swapCase() => convert uppercase to lowercase and vise versa .



