# Basic
for i in range(151):
    print(i)

# Multiples of 5
for j in range(5, 1001, 5):
    print(j)

# Counting the Dojo Way
for i in range(1, 101):
    if (i%10 == 0):
        print("Coding Dojo")
    elif (i%5 == 0):
        print("Coding")
    else:
        print(i)

# Whoa. That Sucker's Huge
sum = 0
for i in range(1, 500001, 2):
    sum += i
print(sum)

# Countdown by Fours
for i in range(2018, 0, -4):
    print(i)

# Flexible Counter
low_num = 2
high_num = 9
mult = 3
for i in range(low_num, high_num+1):
    if(i%mult == 0):
        print(i)
