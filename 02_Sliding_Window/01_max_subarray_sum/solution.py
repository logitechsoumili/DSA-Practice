'''
GeeksforGeeks: https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1

Max Sum Subarray of Size K

Given an array arr[] and a number k,
return the maximum sum of any contiguous
subarray of size k.

Example:

Input:
arr = [100, 200, 300, 400]
k = 2

Output:
700
'''

# ------------------------------------------------------------
# BRUTE FORCE APPROACH [O(n*k)]
# ------------------------------------------------------------
'''
def maxSubarraySum_bruteforce(arr, k):
    max_sum = 0

    for i in range(len(arr) - k + 1):
        curr_sum = 0
        for j in range(i, i + k):
            curr_sum += arr[j]
        max_sum = max(max_sum, curr_sum)

    return max_sum


Approach:
1. Generate every subarray of size k.
2. Calculate its sum from scratch.
3. Track the maximum sum.

Time Complexity: O(n*k)

Space Complexity: O(1)

Not optimal because many elements are
recomputed across overlapping windows.
'''
# ------------------------------------------------------------


# ------------------------------------------------------------
# OPTIMISED APPROACH [Sliding Window]
# O(n)
# ------------------------------------------------------------

class Solution:
    def maxSubarraySum(self, arr, k):
        if len(arr) < k:
            return 0

        # Sum of first window
        window_sum = sum(arr[:k])
        max_sum = window_sum

        # Slide the window
        for i in range(k, len(arr)):

            # Add incoming element and remove outgoing element
            window_sum += arr[i] - arr[i - k]

            max_sum = max(max_sum, window_sum)

        return max_sum


'''
Pattern:
Fixed Size Sliding Window

Key Observation:
Instead of calculating every window sum
from scratch, reuse the previous window's sum.

When the window moves one position:

    New Window Sum
    =
    Previous Window Sum
    - Outgoing Element
    + Incoming Element

This updates the sum in O(1).

Approach:
1. Calculate the sum of the first window of size k.
2. Store it as the current maximum.
3. Slide the window one step at a time.
4. Remove the outgoing element.
5. Add the incoming element.
6. Update the maximum sum.
7. Return the answer.

Time Complexity:
- O(n)

Space Complexity:
- O(1)

Common Mistakes:
1. Recomputing every window sum from scratch.

2. Forgetting to subtract:

       arr[i - k]

3. Forgetting to initialize max_sum using
   the first window.

4. Using nested loops, leading to O(n*k).
'''