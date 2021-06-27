# Look through array
# Set min value to first item
# When smaller item is found, save it
# Shift all items to the left of the index of the new smallest value to the right
# Insert value at the position of the array

def insertion_sort(arr):
    length = len(arr)

    if length <= 1:
        return arr
    
    for i in range(length):
        index = i
        for j in range(i-1, -1, -1):
            if arr[j] > arr[index]:
                arr[index], arr[j] = arr[j], arr[index]
                index = j

    
    return arr

arr1 = []
arr2 = [4]
arr3 = [1, 3, 2, 4]
arr4 = [4, 1, 3, 2]

print(insertion_sort(arr1))
print(insertion_sort(arr2))
print(insertion_sort(arr3))
print(insertion_sort(arr4))

