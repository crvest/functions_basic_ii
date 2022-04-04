# 1. Countdown
array = []
def countdown (start):
    for x in range(start,-1,-1):    # start, stop, step
        array.append(x)
    return array
print(countdown(5))


# 2. Print and Return
def print_and_return (a,b):
    print(a)
    return b
x = print_and_return(1,2)
print(x)

# 3. First Plus Length
def first_plus_length (array):
    return (array[0]+len(array))
print(first_plus_length([1,2,3,4,5]))

# 4. Values Greater than Second
newArray = []
def values_greater_than_second (array):
    count = 0
    if len(array) > 1:  # check for more than 1 element in list
        for x in array:     # iterate through entire list
            if x > array[1]:    # compare element to value at index 1
                count += 1  # increment count if
                newArray.append(x)  # add value to new array if
        print(count)    # print final count
        return newArray # return new array
    else:   # return false if less than two elements
        return False
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# 5. This Length, That Value
def length_and_value (a, b):
    array = []
    for x in range(0, a, 1):
        array.append(b)
    return array
print(length_and_value(4,7))
print(length_and_value(6,2))