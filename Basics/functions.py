# ============================================
# Python Basics - Functions
# ============================================

# functions are instructions packaged together that perform a specific task
# to create a function - def keyword

def hello_func():
    pass # basically want to fill in the function later so we use this keyword
    # basically says that we don't wanna do anything with this for now but we also don't want it to throw any errors for leaving it blank

# executing a function

print(hello_func)
# o/p - <function hello_func at 0x000002A9698EB8A0>
# says at what location in memory the function is

print(hello_func())
# with a paranthesis at the end
# it just gives None as we are not doing anyhting with the function

def hello_function():
    print("Hello Function !")

hello_function() # just executing the function as the print statement is inside the function, no need to print the function like before

def return_func():
    return 'Hello return Function!'
    # return means whenever we execute our function, it is equal to the string

return_func() # if we run this, it doesn't give us any results as it's just a string that we're not doing anything with
print(return_func()) # now it will print our string
print(return_func().upper())

# passing arguments to our function
def greeting_func(greeting):
    return '{} Function'.format(greeting)
    # the greeting variable doesn't affect any variable outside the function, it's scope is only local to the function

print(greeting_func('Hi'))

# if we didn't pass an argument, and don't want it to throw an error, we can specify a default values for when we don't pass an argument

def greet_func(greeting, name = 'You'): # here 'You' is the default value if name is not passed
    return '{}, {}'.format(greeting, name)

print(greet_func('Good Morning', 'All'))
print(greet_func('Good Morning'))



# it is allowing us to accept an arbitrary number of positional or keyword arguments
def student_info(*args, **kwargs):
    print(args) # tuple
    print(kwargs) # dict

student_info('Math', 'Art', name = 'John', age = 22)
# when we print this we see args is a tuple with positional arguments and kwargs is a dictionary with all of our keyword values

courses = ['Math', 'Art']
info = {'name' : 'John', 'age' : 22}
student_info(courses, info) # passed complete list and complete dictionary as positional arguments, hence output is always in a tuple form
# o/p - (['Math', 'Art'], {'name': 'John', 'age': 22}), {} -> a tuple and an empty dict
student_info(*courses, **info) # prints like before if we add stars