'''
15. 3Sum

Given an integer array nums, return all unique triplets
[nums[i], nums[j], nums[k]] such that:

nums[i] + nums[j] + nums[k] == 0

The solution set must not contain duplicate triplets.
'''

# ------------------------------------------------------------
# OPTIMISED APPROACH [O(n²)]
# ------------------------------------------------------------

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        res = []

        for i in range(len(nums) - 2):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            target = -nums[i]

            while left < right:
                s = nums[left] + nums[right]

                if s == target:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while right >= 0 and nums[right] == nums[right + 1]:
                        right -= 1

                elif s < target:
                    left += 1

                else:
                    right -= 1

        return res


'''
Pattern:
Sort + Fix One Element + Two Pointers

Key Observation:
For every element nums[i], we can transform:

    nums[i] + nums[j] + nums[k] = 0

into:

    nums[j] + nums[k] = -nums[i]

This converts the problem into a Two Sum problem on
the remaining part of the sorted array.

Approach:
1. Sort the array.
2. Fix one element nums[i].
3. Use two pointers (left, right) to find pairs whose
   sum equals -nums[i].
4. Skip duplicate values to avoid repeated triplets.
5. Store every valid triplet.

Example:

nums = [-4, -1, -1, 0, 1, 2]

i = -1
target = 1

left = 0
right = 2

0 + 1 = 1 ✓

Triplet = [-1, 0, 1]

Time Complexity:
- Sorting: O(n log n)
- Two-pointer search for each element: O(n²)

Overall: O(n²)

Space Complexity:
- O(1) auxiliary space
- O(k) output space for storing triplets

Common Mistakes:
1. Forgetting to sort the array.
2. Not skipping duplicate i values.
3. Not skipping duplicate left/right values after
   finding a valid triplet.
4. Using a set to remove duplicates when it can be
   avoided with pointer logic.
'''