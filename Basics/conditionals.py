# ============================================
# Python Basics - Conditionals and Booleans
# ============================================

if True:
    print('Conditional was True')
    # prints

if False:
    print('Conditional was False')
    # does not print

language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No Match')

# python doesn't have a switch case as the if elif else statememnts are pretty clean to do the work of a switch statement

# boolean operations

user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in: # AND boolean operation
    print('Admin Page')
else:
    print('Bad Creds')

user = 'Admin'
logged_in = False
if user == 'Admin' or logged_in: # OR boolean operation
    print('Admin Page')
else:
    print('Bad Creds')

user = 'Admin'
logged_in = False
if not logged_in: # NOT boolean operation
    print('Please login')
else:
    print('Welcome')

# object identity : is
# tests if 2 objects have the same identity
# difference between object identity and == ????
# object identity checks if they're the same object in memory

a = [1,2,3]
b = [1,2,3]
print(a==b)
print(a is b) # this will return false as they are different locations in memory

# to print memory location where they're stored at
print(id(a))
print(id(b))

b = a
print(a==b)
print(a is b)
print(id(a))
print(id(b))
print(id(a) == id(b))

# all the things in python that evaluate to false values (rest all are true)
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), []
    # Any empty mapping. For example, {}

