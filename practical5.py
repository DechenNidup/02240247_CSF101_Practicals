# Implementing Linear and Binary Search Algorithms 

# 1. Implement Linear Search
def linear_search(array,target):
    for i in range(len(array)):
        if array[i]==target:
            return i
    return("Not there")
test_array=[2,3,4,5,6,7]
result=linear_search(test_array,5)
print(result)
        
# 2. Implement Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Return -1 if the target is not in the list
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Test the function
test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}")

# EXERCISE
# 1. Modify the linear search function to return all indices where the target appears, not just the first one.
def linear_search(array, target):
    result = []
    for i in range(len(array)):
        if array[i] == target:  
            result.append(i)    
    return result if result else "Not Found"

sample_array = [1, 3, 5, 2, 3, 8, 3, 5, 3, 4, 2]
result = linear_search(sample_array, 3)
print(result)

# 2. Implement a function that uses binary search to find the insertion point for a target value in a sorted list.
def find_insertion_point(arr, target):
    low = 0
    high = len(arr)
    
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
            
    return low  
sorted_list = [1, 3, 5, 7, 9]
target = 6
index = find_insertion_point(sorted_list, target)
print(index)  
sorted_list.insert(index, target)
print(sorted_list)

# 3. Create a function that counts the number of comparisons made in each search algorithm.
def linear_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons

# Test data
my_list = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

# Run linear search
lin_index, lin_comps = linear_search(my_list, target)

# Run binary search
bin_index, bin_comps = binary_search(my_list, target)

# Show results
print("Linear Search")
print("Found at index:", lin_index)
print("Comparisons made:", lin_comps)

print("Binary Search ")
print("Found at index:", bin_index)
print("Comparisons made:", bin_comps)

# 4. Implement a jump search algorithm and compare its performance with linear and binary search.
import math

# Linear Search
def linear_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

# Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons

# Jump Search
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # jump size
    prev = 0
    comparisons = 0

    # Jumping through blocks
    while prev < n and arr[min(step, n)-1] < target:
        comparisons += 1
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1, comparisons

    # Linear search inside the block
    for i in range(prev, min(step, n)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons

    return -1, comparisons

# Test list (must be sorted for binary and jump search)
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
target = 15

# Run all searches
lin_index, lin_comps = linear_search(my_list, target)
bin_index, bin_comps = binary_search(my_list, target)
jmp_index, jmp_comps = jump_search(my_list, target)

# Print results
print("Linear Search")
print("Found at index:", lin_index)
print("Comparisons:", lin_comps)

print("Binary Search")
print("Found at index:", bin_index)
print("Comparisons:", bin_comps)

print("Jump Search ")
print("Found at index:", jmp_index)
print("Comparisons:", jmp_comps)



