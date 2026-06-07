'''
75. Sort Colors

Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order:

    0 (Red)
    1 (White)
    2 (Blue)

You must solve this problem without using the library sort function.

Example:

Input:
nums = [2,0,2,1,1,0]

Output:
[0,0,1,1,2,2]
'''

# ------------------------------------------------------------
# BRUTE FORCE APPROACH [O(n) Space]
# ------------------------------------------------------------
'''
def sortColors_bruteforce(nums):

    zeros = []
    ones = []
    twos = []

    for num in nums:
        if num == 0:
            zeros.append(num)

        elif num == 1:
            ones.append(num)

        else:
            twos.append(num)

    nums[:] = zeros + ones + twos


Approach:
1. Create separate arrays for 0s, 1s and 2s.
2. Traverse the array and place each element into
   its respective bucket.
3. Concatenate all buckets.

Time Complexity: O(n)

Space Complexity: O(n)

Not optimal because extra arrays are used.
'''
# ------------------------------------------------------------


# ------------------------------------------------------------
# BETTER APPROACH [Counting]
# O(n) Time | O(1) Space
# Two Passes
# ------------------------------------------------------------
'''
def sortColors_counting(nums):

    count0 = count1 = count2 = 0

    for num in nums:

        if num == 0:
            count0 += 1

        elif num == 1:
            count1 += 1

        else:
            count2 += 1

    idx = 0

    for _ in range(count0):
        nums[idx] = 0
        idx += 1

    for _ in range(count1):
        nums[idx] = 1
        idx += 1

    for _ in range(count2):
        nums[idx] = 2
        idx += 1


Approach:
1. Count the number of 0s, 1s and 2s.
2. Overwrite the array using these counts.

Time Complexity: O(n)

Space Complexity: O(1)

Better than brute force because no extra arrays
are used.

Still requires two passes.
'''
# ------------------------------------------------------------


# ------------------------------------------------------------
# OPTIMISED APPROACH [Dutch National Flag]
# O(n) Time | O(1) Space
# Single Pass
# ------------------------------------------------------------

class Solution:
    def sortColors(self, nums: list[int]) -> None:

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:

                nums[low], nums[mid] = nums[mid], nums[low]

                low += 1
                mid += 1

            elif nums[mid] == 1:

                mid += 1

            else:  # nums[mid] == 2

                nums[mid], nums[high] = nums[high], nums[mid]

                high -= 1


'''
Pattern:
Two Pointers / Dutch National Flag

Key Observation:
The array contains only:

    0, 1, 2

Instead of sorting, we partition the array
into three regions.

Regions:

    [0, low)       -> all 0s
    [low, mid)     -> all 1s
    [mid, high]    -> unexplored
    (high, end]    -> all 2s

Approach:
1. Maintain three pointers:

       low
       mid
       high

2. If nums[mid] == 0:
       swap with low
       move both low and mid

3. If nums[mid] == 1:
       move mid

4. If nums[mid] == 2:
       swap with high
       move high

       Do NOT move mid because the swapped
       element has not been processed yet.

Example:

nums = [2,0,2,1,1,0]

Initial:

low = 0
mid = 0
high = 5

[2,0,2,1,1,0]

Swap 2 with high:

[0,0,2,1,1,2]

Process again at mid.

Eventually:

[0,0,1,1,2,2]

Time Complexity:
- O(n)

Space Complexity:
- O(1)

Common Mistakes:
1. Incrementing mid after swapping with high.

   Wrong:

       swap(mid, high)
       high -= 1
       mid += 1

2. Forgetting that the swapped value at mid
   still needs to be processed.

3. Using sort() instead of solving in-place.

Progression:

Brute Force:
Buckets for 0s, 1s, 2s
Time: O(n)
Space: O(n)

↓

Counting Approach:
Count frequencies and overwrite array
Time: O(n)
Space: O(1)

↓

Dutch National Flag:
Single traversal
Time: O(n)
Space: O(1)

This is the optimal interview solution.
'''
```
