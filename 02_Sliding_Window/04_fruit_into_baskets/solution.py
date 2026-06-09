'''
904. Fruit Into Baskets

You are given an integer array fruits where fruits[i]
represents the type of fruit produced by the ith tree.

You have two baskets, and each basket can hold only
one type of fruit.

Starting from any tree, you must pick exactly one fruit
from every tree while moving to the right.

Return the maximum number of fruits you can collect.
'''

# ------------------------------------------------------------
# BRUTE FORCE APPROACH [O(n²)]
# ------------------------------------------------------------
'''
def totalFruit_bruteforce(fruits):
    max_fruits = 0

    for i in range(len(fruits)):
        basket = set()

        for j in range(i, len(fruits)):
            basket.add(fruits[j])

            if len(basket) > 2:
                break

            max_fruits = max(max_fruits, j - i + 1)

    return max_fruits


Approach:
1. Start a subarray from every index.
2. Keep extending it to the right.
3. Track distinct fruit types using a set.
4. If fruit types exceed 2:
       - Stop extending the current subarray.
5. Update the maximum valid length.
6. Return the longest valid length.

Time Complexity: O(n²)

Space Complexity: O(1)
'''
# ------------------------------------------------------------


# ------------------------------------------------------------
# OPTIMISED APPROACH [Variable Size Sliding Window]
# O(n)
# ------------------------------------------------------------

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_fruits = 0
        basket = {}

        for right in range(len(fruits)):
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits


'''
Pattern:
Variable Size Sliding Window

Key Observation:
We can only keep at most 2 distinct fruit types
inside our baskets.

This means we need the longest contiguous subarray
containing at most 2 distinct elements.

Expand the window by moving the right pointer.

Whenever the number of distinct fruit types
exceeds 2, shrink the window from the left
until it becomes valid again.

Track the largest valid window seen so far.

Approach:
1. Initialize left pointer and frequency map.
2. Expand the window using right pointer.
3. Add the current fruit to the basket.
4. If distinct fruit types exceed 2:
       - Shrink the window from the left.
       - Remove fruit types whose count
         becomes zero.
5. Update maximum window length.
6. Return the largest valid window.

Time Complexity:
- O(n)

Each fruit enters and leaves the window
at most once.

Space Complexity:
- O(1)

At most 3 fruit types are stored in the map
before shrinking.

Common Mistakes:
1. Thinking the answer is the number of
   fruit types instead of total fruits.

2. Forgetting to delete a fruit type when
   its frequency becomes zero.

3. Using if instead of while when the
   basket contains more than 2 fruit types.

4. Updating the answer before making
   the window valid.
'''