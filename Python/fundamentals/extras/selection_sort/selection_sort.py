# Loop through array
# compare value at index to the value at the next spot
# if the value at the next spot is smaller than the value at the index, swap it to the front of the array
# increment the front index to the latest sorted index and repeat until the array is sorted

def selection_sort(arr):
    # Check for an empty array or an array with only one element  
    if len(arr) <= 1:
        return arr
    
    length = len(arr)
    for i in range(length):
        min = arr[i] # Start with a min value
        # Look for a new min
        for j in range(i+1, length):
            if arr[j] < min:
                min = arr[j] # set the new min
                arr[j], arr[i] = arr[i], arr[j] # Swap the values
    return arr


arr1 = []
arr2 = [3]
arr3 = [2, 6, 3, 7, 5, 4]
arr4 = [6, 5, 1, 2, 4, 3]

print(selection_sort(arr1))
print(selection_sort(arr2))
print(selection_sort(arr3))
print(selection_sort(arr4))
