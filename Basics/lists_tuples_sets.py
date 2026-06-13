# ============================================
# Python Basics - Lists, Tuples, Sets
# ============================================

# list and tuples - sequential data
# sets - unordered collections of values with no duplicates


# *********************** lists ***********************


courses = ['History' , 'Math' , 'Physics' , 'CompSci']
print(courses)

# how many values in list
print(len(courses))

# accessing individual values (0 based indexing)
print(courses[0]) # first
print(courses[3]) # last

# can also use negative indexing
print(courses[-1]) # -1 prints last item, so we don't have to worry about the length of the list

# accessing range of values
# 1st index inclusive, 2nd index not inclusive
print(courses[0:2]) # want all of values between beginning and upto (not including) the second index
print(courses[:2]) # assumes we want from start
print(courses[2:]) # assumes we want to go all the way to the end of the list

# adding an item to our list
courses.append('Art') # adds to end
print(courses)

# adding to a specific location - INSERT(location, value)
courses.insert(1, 'Art')
print(courses)

courses2 = ['Art' , 'Education'] # want to add to our original courses list
courses.insert(0, courses2)
print(courses)
# it adds the entire list of courses2 and not each individual value
print(courses[0]) # the first value will be the list itself

# hence use the extend method
courses.extend(courses2) # adds value in end
print(courses)

# if we do append instead of extend, it will append the list itself and not individual elements
# we need to EXTEND for it to add each singular element

# removing an item
courses.remove('Math') # removes math
courses.pop() # by default removes the last value (like stack)
# pop retirns the value it removed so we can set a variable and grab that returned value
popped = courses.pop()
print(popped)
print(courses)

#sorting

courses = ['History' , 'Math' , 'Physics' , 'CompSci']
nums = [ 1, 5, 4, 3]

# reversing our list
courses.reverse()
nums.reverse()
print(courses)
print(nums)

# sorting
courses.sort()
nums.sort()
print(courses)
print(nums) # sorted in ascending order

# to sort in descending
courses.sort(reverse = True)
nums.sort(reverse = True)
print(courses)
print(nums)

# all of the above are sorting in the original list itself, what if we dont want to do the operations in the original list
# instead of calling the sort method on out list, we'll use the sorted function

sorted(courses)
print(courses) # won't be sorted as the aorted function doesn't sort the list in place, instead it returns a sorted verion of the list
sorted_list = sorted(courses)
print(sorted_list)

# general
print(min(nums))
print(max(nums))
print(sum(nums))

# finding values

print(courses.index('CompSci'))
# if we try to print index of a value that doesn't exist, we get a value error

# wanna check true or false if there in list or not
print('Art' in courses)
print('Math' in courses)

# looping values
for item in courses:
    print(item) # prints each in new line as print statement by default goes to new line when executed

# instead of just getting the course, if we want the index as well - enumerate function
for index, course in enumerate(courses): # 'course' is a variable just like 'item'
    print(index, course)

# if don't want to start with a zero, we can pass a start value to the enumerate function
for index, course in enumerate(courses, start=1):
    print(index, course)

# converting list to string
course_str = ', '.join(courses)
print(course_str) # we get out values individually seperated by a comma

# opposite of that - turn a string bac to a list
new_list = course_str.split(', ')
print(new_list)

# *********************** tuples ***********************

# tuples are v similar to lists - be we can;t modify them
# in programming this is called mutable or immutable
# mutable - lists
# immutable - tuple

list1 = ['History' , 'Math' , 'Physics' , 'CompSci']
list2 = list1

print(list1)
print(list2) 

list1[0] = 'Art'
print(list1)
print(list2) # also shows changes even though we only changed in list1
# this is because both are the same mutable object

# hence if we want a list of values which we know are going to change, then we need a tuple

tuple1 = ('History' , 'Math' , 'Physics' , 'CompSci')
tuple2 = tuple1

print(tuple1)
print(tuple2)

# tuple1[0] = 'Art'
# if we do this - we get a type error saying tuple does not support item assignment, this is because it's immutable
# as tuple is immutable, it does not have as many methods as a list, as most methods involved mutating the values

# *********************** sets ***********************

# sets are values that are unordered and also have no duplicates

cs_courses = {'History' , 'Math' , 'Physics' , 'CompSci'}
print(cs_courses) # doesn't print in the order we added them
# o/p - {'CompSci', 'History', 'Math', 'Physics'}
# and if we run it a couple of times, that order can change with each execution

# this is because order doesn't really matter in sets
# we mostly use sets to check if a value belongs in a set or to remove duplicates, as a set throws out duplicates

# duplicates
cs_courses = {'History' , 'Math' , 'Physics' , 'CompSci', 'Math'}
print(cs_courses)
# will not print Math twice

# to check if belong in set or no
print('Math' in cs_courses) # returns true or false

# sets can also determine what values we share or don't share with other sets
art_courses = {'History' , 'Math' , 'Art' , 'Design'}
print(cs_courses.intersection(art_courses)) # shows what courses are in cs AND art
print(cs_courses.difference(art_courses)) # prints which are in cs but not in art

# combine both sets and print all courses offered - UNION
print(cs_courses.union(art_courses))







# empty lists, tuples and sets

# empty list
empty_list = []
empty_list = list()

# empty tuples
empty_tuples = ()
empty_tuples = list()

# empty set
empty_set = {} # -> this does not create an empty set, it creates an empty dictionary
empty_set = list()















