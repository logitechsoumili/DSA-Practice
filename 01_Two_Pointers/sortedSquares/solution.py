'''
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
'''

#---------------------------------------------------------------------------------------

# BRUTE FORCE APPROACH [O(nlogn)]
'''
def sortedSquares_bruteforce(arr):
    new = [x**2 for x in arr]
    new.sort()
    return new
'''

'''
Approach:
1. Square every element in the array.
2. Sort the resulting squared array.

Time Complexity:
- Squaring all elements takes O(n)
- Sorting takes O(n log n)
Overall Time Complexity: O(n log n)

Space Complexity: O(n) (new list created to store squared values)

Not time optimal because it uses sorting after squaring,
even though the original array is already sorted.
'''

#---------------------------------------------------------------------------------------

# MERGED APPROACH [O(n)]
'''
def sortedSquares_merge(arr):
    if not arr:
        return []

    neg, pos = [], []

    for i in range(len(arr)-1): # case where negative and positive elements are both present
        if arr[i] < 0 and arr[i+1] >= 0:
            neg = [x**2 for x in arr[:i+1]][::-1]
            pos = [x**2 for x in arr[i+1:]]
            break

    if not neg and not pos: # case when all elements are either positive or negative
        if arr[0] >= 0:
            pos = [x**2 for x in arr]
            return pos
        else:
            neg = [x**2 for x in arr]
            return neg[::-1]

    res = []
    i, j = 0, 0

    while (i < len(neg) and j < len(pos)):
        if neg[i] <= pos[j]:
            res.append(neg[i])
            i += 1
        else:
            res.append(pos[j])
            j += 1

    while (i < len(neg)):
        res.append(neg[i])
        i += 1

    while (j < len(pos)):
        res.append(pos[j])
        j += 1

    return res
'''

'''
Approach:
1. Find the split point between negative and non-negative numbers.
2. Square both parts separately.
3. Merge the squared arrays using two-pointer technique.

Time Complexity: O(n)
Space Complexity: O(n) (extra arrays used for merging)

Not space optimal because it uses additional lists instead of modifying in-place.
'''

#---------------------------------------------------------------------------------------

# OPTIMISED APPROACH [O(n)]
def sortedSquares_twoPointer(arr):
    res = []
    i, j = 0, len(arr) - 1

    while i <= j:
        if arr[i]**2 >= arr[j]**2:
            res.append(arr[i]**2)
            i += 1
        else:
            res.append(arr[j]**2)
            j -= 1
    return res[::-1]

L = list(map(int, input("Enter sorted array: ").split()))
print(sortedSquares_twoPointer(L))

'''
Approach:
1. Use two pointers at the beginning and end of the array.
2. Compare the squares of both elements.
3. Insert the larger square into the result array.
4. Move the corresponding pointer inward.
5. Reverse the result since larger squares are added first.

Time Complexity: O(n)
- Each element is processed exactly once.

Space Complexity: O(n)
- A new result array is used to store squared values.

This is the most optimal approach in terms of time,
and uses only one extra array without creating intermediate lists.
'''