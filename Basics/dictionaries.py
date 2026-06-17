# ============================================
# Python Basics - Dictionaries
# ============================================

# allows to work with key value pairs
# like hashmaps or associative arrays

# key value pairs - 2 values, where the key is the unique identifier where we can find our data, and the value is our data

# key : value
student = {'name' : 'John' , 'age' : 25 , 'courses' : ['Math', 'CompSci']}
print(student)

# want to access name
print(student['name'])
print(student['courses'])

# if we try to access a key that doesn't exist, we get a key error
# but what if we don't want it to throw an error everythime we try to access a key which doesn't exist, what if we want it to return none or a default value
# for this we can access using the get method

print(student.get('phone')) # by default the get method returns 'None' instead of an error, and we can also change this default value

print(student.get('phone', 'Not found')) # 2nd argument will be the default of doesn't exist

# adding new entry to our dictionary
student['phone'] = '1111-1212-04'
print(student.get('phone'))
# in the above case, if the key already exists, it will update the value of that key

student['name'] = 'Lassi'
print(student)

# to update multiple values at a time -> use update method
student.update({'name' : 'Luna' , 'age' : 20 , 'phone' : '1111-1212-04'})
print(student)

# delete specific key and its value
# method 1 - del keyword
del student['age']
print(student)
# method 2 - pop method, will remove as well as return the value, hence can store it in a variable
phone = student.pop('phone')
print(student)
print(phone)

# looping through all the keys and values in our dictionary
student = {'name' : 'John' , 'age' : 25 , 'courses' : ['Math', 'CompSci']}

# to find how many keys we have - len function
print(len(student))

# print keys
print(student.keys())

# print values
print(student.values())

# keys and values
print(student.items())
# prints out in form of pairs

for key in student:
    print(key)
    # here it just prints out the keys, it just looped through the keys

# if we want to loop throught the keys and the values, need to use the items method as it comes as a pair

for key, value in student.items():
    print(key, value)