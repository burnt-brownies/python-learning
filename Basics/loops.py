# ============================================
# Python Basics - Loops & Iterations
# ============================================

nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

# break - completely breaks out of the loop
# continue - moves on to the next iteration of the loop

for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

# it will keep printing till it encounters 3, when 3 encounters it will just print Found! and then break out of the loop

for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)
# for 1 and 2 it printed the numbers, when 3 encountered it just printed Found! and then did not print the number 3 as we did continue, i just skipped rest of the loop and went to the next

# loop within a loop

for num in nums:
    for letter in 'abc':
        print(num, letter)

# wanna go through a loop for a certain number of times - we use the builtin function called range

for i in range(10):
    print(i) # prints 0 to 9
# if don't want to start with a zero, we can also pass a starting value in the range
for i in range(1, 10):
    print(i) # print 1 to 9 

# while loops
# will keep going until a certain condition is met or until a break is encountered

x = 0 
while x < 10 :
    print(x)
    x += 1

# break in while loop

x = 0 
while x < 10 :
    if x == 5:
        break
    print(x)
    x += 1

# if we want an infinite loop which we only want to end once a condition is encountered

while True:
    if x == 5 :
        break
    print(x)
    x += 1



