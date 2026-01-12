'''
167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
'''

# BRUTE FORCE SOLUTION (O(n^2); unsorted)
'''
def brute_force(arr, target):
    sum_ = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return (i, j)
    return None
'''

# BETTER SOLUTION (O(n); unsorted)
'''
def better(arr, target):
    index_map = {}
    for i, val in enumerate(arr):
        comp = target - val
        if comp in index_map:
            return index_map[comp], i
        index_map[val] = i
'''

# OPTIMISED SOLUTION (O(n); sorted)
def optimised(arr, target):
    i, j = 0, len(arr) - 1
    while i < j:
        res = arr[i] + arr[j]
        if res == target:
            return (i, j)
        elif res < target:
            i += 1
        else:
            j -= 1

L = list(map(int, input("Enter a sorted array: ").split()))
target = int(input("Enter target: "))
print(optimised(L, target))