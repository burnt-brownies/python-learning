# ============================================
# Python Basics - Strings
# ============================================

# put string in a variable called message
message = 'Hello World' 
print(message) 

# both will have same output
print('Hello World')

# single and double quotes
# print('She's writing code) - will give an error as after the 'She' it thinks the string has ended, hence in cases like these we use double quotes
print("She's writing code")

# or can also escape that single quote with a backslash, now python knows that the single quote doesn't close out the string and instead the last one should
print('She\'s writing code')

# multi line string
multiLine = """She's writing code
in Python"""
print(multiLine)

# length of a word
print(len(message))

# accessing characters individually
print(message[0])
print(message[1])
print(message[2])
print(message[3])
print(message[4])

# last character will be at length - 1 as indexing starts from 0
print(message[10])

# if tried to access out of range characters, e.g. 11 -> will throw an error

# range of characters -> first index - starting point (inclusive) , second index - ending point(non inclusive)
print(message[0:5])
# prints from 0 to 4th index

print(message[:5])
# leaving out start index assumes that we want it from start

print(message[6:])
# leaving out stop index goes all the way till the end

# return copy of string with all lowercase / uppercase
print(message.lower())
print(message.upper())
print(message) # doesn't change anything in original string, just copies and returns

# counting frequency 
print(message.count('Hello')) # will print 1 as only 1 Hello there
print(message.count('l')) # will print 3 as 3 'l' are there

# to find index of certain words/characters
print(message.find('World')) # world starts at the 6th index
print(message.find('l')) # 1st occurence of 'l' at index 2
print(message.find('Hi')) # will return a -1 as that string doesn't exist

# replacing characters
# takes 2 arguments -> (what we wanna replace, what we wanna replace it with)
message.replace('World' , 'Universe')
print(message) 
# will still print Hello World
# why?? the replace fucntion returns a new string with the value replaced, it doesn't change anything in the original string, hence we need to set a new variable, so that the replaced string is returned in that
new_message = message.replace('World' , 'Universe')
print(new_message) # now prints Hello Universe(replaced)
# if wan to change in the same message variable, set message = message.replace()

# adding and concatentaing strings
greeting = 'Hello'
name = 'Michael'

message = greeting + name 
print(message)
# will print HelloMichael -> it combines, but it doesn't have a space there, hence add a string between then which spaces them out
message = greeting + ', ' + name
print(message)
message = greeting + ', ' + name + '. Welcome!'
print(message)

# + sign always isn't the best method, for eg - for longer strings we cannot + each and every word
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)
# curly brackets -> placeholders

# another method to do the same -> fstrings
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)
# can directly pass variables in placeholders, can do operations like uppercase and lowercase in placeholders itself

print(dir(name)) # shows what all fucntions we can perform with the name variable
print(help(str)) # shows what all operations we can perform with string class
