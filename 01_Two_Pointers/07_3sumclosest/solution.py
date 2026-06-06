'''
16. 3Sum Closest

Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
'''

# ------------------------------------------------------------
# OPTIMISED APPROACH [O(n²)]
# ------------------------------------------------------------

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        min_diff = float('inf')
        res_sum = 0

        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]
                d = abs(total - target)

                # Update answer if a closer sum is found
                if d < min_diff:
                    min_diff = d
                    res_sum = total

                # Exact match found
                if total == target:
                    return res_sum

                elif total < target:
                    left += 1

                else:
                    right -= 1

        return res_sum


'''
Pattern:
Sort + Fix One Element + Two Pointers

Key Observation:
Unlike 3Sum, we do not need to find all valid triplets.

Instead, we keep track of:
1. The closest difference from the target.
2. The corresponding triplet sum.

Approach:
1. Sort the array.
2. Fix one element nums[i].
3. Use two pointers to explore possible triplets.
4. Compute:

       total = nums[i] + nums[left] + nums[right]

5. Compare:

       abs(total - target)

   with the current minimum difference.

6. Update the answer whenever a closer sum is found.
7. If an exact match is found, return immediately.

Example:

nums = [-1, 2, 1, -4]
target = 1

Sorted:

[-4, -1, 1, 2]

Triplets:
(-4, -1, 2) = -3
(-4, 1, 2)  = -1
(-1, 1, 2)  = 2

Closest sum = 2

Time Complexity:
- Sorting: O(n log n)
- Two-pointer traversal: O(n²)

Overall: O(n²)

Space Complexity:
- O(1)

Difference from 3Sum:
3Sum:
- Store all valid triplets.
- Handle duplicates.
- Look for exact sum = 0.

3Sum Closest:
- Store only the best sum.
- No duplicate handling required.
- Track minimum difference from target.

Common Mistakes:
1. Returning the difference instead of the sum.
2. Forgetting to update the answer before moving pointers.
3. Using only positive differences instead of:

       abs(total - target)

4. Not returning immediately when an exact match is found.


3Sum:
Fix one element → find pair with sum = -nums[i]

3Sum Closest:
Fix one element → find pair that makes the total
closest to target
'''