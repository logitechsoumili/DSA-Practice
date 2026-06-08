'''
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is greater than or
equal to target.

If there is no such subarray, return 0.
'''

# ------------------------------------------------------------
# BRUTE FORCE APPROACH [O(n²)]
# ------------------------------------------------------------
'''
def minSubArrayLen_bruteforce(target, nums):

    min_len = float('inf')

    for i in range(len(nums)):

        curr_sum = 0

        for j in range(i, len(nums)):

            curr_sum += nums[j]

            if curr_sum >= target:
                min_len = min(min_len, j - i + 1)
                break

    return 0 if min_len == float('inf') else min_len


Approach:
1. Start a subarray from every index.
2. Keep extending it until the sum reaches target.
3. Update the minimum length.
4. Return the smallest valid length.

Time Complexity: O(n²)

Space Complexity: O(1)
'''
# ------------------------------------------------------------


# ------------------------------------------------------------
# OPTIMISED APPROACH [Variable Size Sliding Window]
# O(n)
# ------------------------------------------------------------

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_len = float('inf')

        left = 0
        window_sum = 0

        for right in range(len(nums)):

            window_sum += nums[right]

            while window_sum >= target:

                min_len = min(min_len, right - left + 1)

                window_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len


'''
Pattern:
Variable Size Sliding Window

Key Observation:
Unlike fixed-size sliding window problems,
the window size is not predetermined.

Expand the window until the sum becomes
greater than or equal to target.

Once the condition is satisfied,
shrink the window from the left while
maintaining the condition.

This helps find the minimum valid window.

Approach:
1. Initialize left pointer and window sum.
2. Expand the window using right pointer.
3. Add nums[right] to the current sum.
4. While the window sum is valid:
       - Update minimum length.
       - Remove nums[left].
       - Move left forward.
5. Return the minimum length found.

Time Complexity:
- O(n)

Each element enters and leaves the window
at most once.

Space Complexity:
- O(1)

Common Mistakes:
1. Using a fixed-size window approach.

2. Forgetting to shrink the window after
   reaching the target.

3. Updating min_len after shrinking
   instead of before.

4. Returning float('inf') when no valid
   subarray exists instead of returning 0.
'''