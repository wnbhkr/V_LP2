def selectionSort(array, size):
    # Iterate through each index of the array
    for ind in range(size):
        min_index = ind
        # Find the index of the smallest element in the remaining unsorted portion of the array
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        # Swap the smallest element with the current element
        (array[ind], array[min_index]) = (array[min_index], array[ind])

# Initialize the array to be sorted
arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
# Get the size of the array
size = len(arr)
# Call the selectionSort function to sort the array
selectionSort(arr, size)
# Print the sorted array
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)


'''

The comments have been added to provide a clear understanding of each part of the code:

1. The `selectionSort` function takes two inputs: `array` - the array to be sorted, and `size` - the size of the array.

2. The outer loop `for ind in range(size):` iterates through each index of the array.

3. Inside the outer loop, the variable `min_index` is set to the current index (`ind`).

4. The inner loop `for j in range(ind + 1, size):` starts from the next index after `ind` and iterates through the remaining elements of the array.

5. In the inner loop, the code compares each element at index `j` with the element at `min_index`. If the element at `j` is smaller, `min_index` is updated to `j`.

6. After the inner loop, the code performs a swap operation to place the smallest element found at `min_index` in its correct position by swapping it with the element at the current index (`ind`). This is done using the tuple assignment `(array[ind], array[min_index]) = (array[min_index], array[ind])`.

7. The array is sorted in ascending order after the completion of the outer loop.

8. The array `arr` is initialized with the provided values.

9. The `len(arr)` function is used to determine the size of the array, which is stored in the `size` variable.

10. The `selectionSort` function is called with the `arr` and `size` variables as arguments to perform the sorting operation.

11. Finally, the sorted array is printed using the `print` statement.

The output of the code will be the sorted array in ascending order. In this case, it will be `[-202, -97, -9, -2, 0, 11, 45, 88, 747]`.
'''