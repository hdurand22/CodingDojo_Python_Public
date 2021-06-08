# Countdown
def countdown(num):
    num_list = []
    for i in range(num, -1, -1):
        num_list.append(i)
    return num_list

# Print and Return
def print_and_return(list):
    print(list[0])
    return(list[1])

# First Plus Length
def first_plus_length(arr):
    return(arr[0]+len(arr))

# Values Greater Than Second
def values_greater_than_second(list):
    if (len(list) < 2):
        return False
    else:
        new_list = []
        second_val = list[1]
        count = 0
        for i in list:
            if (i > second_val):
                count += 1
                new_list.append(i)
        print(count)
        return new_list

# This Length, That Value
def this_length_that_value(size, value):
    new_list = []
    for i in range(0, size):
        new_list.append(value)
    return new_list
