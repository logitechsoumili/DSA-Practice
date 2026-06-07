'''
Triplets with Smaller Sum

Given an array arr[] of distinct integers and a value sum,
find the count of triplets (i, j, k), having (i < j < k)
such that:

    arr[i] + arr[j] + arr[k] < sum

Examples:

Input:
sum = 2
arr = [-2, 0, 1, 3]

Output:
2

Explanation:
Valid triplets:
(-2, 0, 1)
(-2, 0, 3)
'''

# ------------------------------------------------------------
# OPTIMISED APPROACH [O(n²)]
# ------------------------------------------------------------

class Solution:
    def countTriplets(self, sum, arr):
        arr.sort()
        ans = 0

        for i in range(len(arr) - 2):

            left = i + 1
            right = len(arr) - 1

            while left < right:

                total = arr[i] + arr[left] + arr[right]

                if total >= sum:
                    right -= 1

                else:
                    ans = ans + (right - left)
                    left += 1

        return ans


'''
Pattern:
Sort + Fix One Element + Two Pointers

Key Observation:
After fixing arr[i], the problem becomes finding
pairs (left, right) such that:

    arr[i] + arr[left] + arr[right] < sum

Since the array is sorted, if:

    arr[i] + arr[left] + arr[right] < sum

then every element between left and right will
also form a valid triplet with arr[i] and arr[left].

Therefore, instead of checking each triplet
individually, we can directly count:

    right - left

triplets at once.

Approach:
1. Sort the array.
2. Fix one element arr[i].
3. Use two pointers:
      left = i + 1
      right = n - 1
4. Calculate the current triplet sum.
5. If the sum is too large:
      move right leftwards.
6. If the sum is smaller than the target:
      count all valid triplets using:

          right - left

      then move left forward.
7. Return the total count.

Example:

arr = [-2, 0, 1, 3]
sum = 2

i = -2
left = 0
right = 3

Current Triplet:
(-2, 0, 3)

Current Sum = 1

Since 1 < 2:

(-2, 0, 3)
(-2, 0, 1)

are both valid.

Count:

    right - left
    = 3 - 1
    = 2

Time Complexity:
- Sorting: O(n log n)
- Two Pointer Traversal: O(n²)

Overall: O(n²)

Space Complexity:
- O(1)

Common Mistakes:
1. Using:

       ans += 1

   instead of:

       ans += (right - left)

2. Forgetting to sort the array.

3. Moving left when the sum is too large.

4. Trying to store all triplets instead of
   counting them.

Connection with Previous Problems:

3Sum:
- Find exact triplets whose sum equals target.

3Sum Closest:
- Find the triplet whose sum is closest to target.

Triplets Smaller Sum:
- Count all triplets whose sum is smaller
  than the target.

The most important line in this problem is:

    ans += (right - left)

Understanding why this works is the key to
understanding the entire algorithm.
'''