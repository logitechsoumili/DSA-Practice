'''
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

You must do this in-place without making a copy of the array.

Example:

Input:
nums = [0,1,0,3,12]

Output:
[1,3,12,0,0]
'''

# ------------------------------------------------------------
# OPTIMISED APPROACH [O(n)]
# ------------------------------------------------------------

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        curr = 0  # position where next non-zero should be placed

        for nxt in range(len(nums)):
            if nums[nxt] != 0:
                nums[curr], nums[nxt] = nums[nxt], nums[curr]
                curr += 1


'''
Pattern:
Two Pointers (Read Pointer + Write Pointer)

Key Observation:
We do not care about the positions of zeros.

We only need to:
1. Preserve the order of non-zero elements.
2. Move all zeros to the end.

Approach:
Use two pointers:

curr:
    Points to the position where the next
    non-zero element should be placed.

nxt:
    Scans the array from left to right.

Whenever a non-zero element is found:

    swap(nums[curr], nums[nxt])

and move curr forward.

Example:

nums = [0,1,0,3,12]

Initial:

curr = 0

nxt = 1

Found:

    nums[1] = 1

Swap:

    [1,0,0,3,12]

curr = 1

--------------------------------

nxt = 3

Found:

    nums[3] = 3

Swap:

    [1,3,0,0,12]

curr = 2

--------------------------------

nxt = 4

Found:

    nums[4] = 12

Swap:

    [1,3,12,0,0]

Done.

Time Complexity:
- O(n)

Each element is visited exactly once.

Space Complexity:
- O(1)

No extra array is used.

Common Mistakes:
1. Using an extra array to store non-zero elements.

2. Forgetting that the relative order of
   non-zero elements must remain unchanged.

3. Maintaining two scanning pointers instead
   of a write pointer and a read pointer.

Why It Works:

At every step:

    nums[0 : curr]

contains all non-zero elements seen so far
in their correct relative order.

The remaining part of the array contains
unprocessed elements and zeros.

Connection with Previous Problems:

Remove Duplicates:
- Write valid elements to the front.

Move Zeroes:
- Write non-zero elements to the front.

Sort Colors:
- Partition the array into regions.

All three use the idea of maintaining
a boundary pointer while scanning the array.
'''