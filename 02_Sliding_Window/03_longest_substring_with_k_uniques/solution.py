'''
GeeksforGeeks: https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

Longest Substring with K Uniques

Given a string s consisting only of lowercase alphabets and an integer k,
find the length of the longest substring that contains exactly k distinct
characters.

If no such substring exists, return -1.
'''

# ------------------------------------------------------------
# BRUTE FORCE APPROACH [O(n²)]
# ------------------------------------------------------------
'''
def longestKSubstr_bruteforce(s, k):
    max_len = -1

    for i in range(len(s)):
        unique_chars = set()

        for j in range(i, len(s)):
            unique_chars.add(s[j])

            if len(unique_chars) == k:
                max_len = max(max_len, j - i + 1)

            elif len(unique_chars) > k:
                break

    return max_len


Approach:
1. Start a substring from every index.
2. Keep extending it character by character.
3. Track distinct characters using a set.
4. If distinct characters become exactly k:
       - Update maximum length.
5. If distinct characters exceed k:
       - Stop extending that substring.
6. Return the longest valid length.

Time Complexity: O(n²)

Space Complexity: O(k)
'''
# ------------------------------------------------------------


# ------------------------------------------------------------
# OPTIMISED APPROACH [Variable Size Sliding Window]
# O(n)
# ------------------------------------------------------------

class Solution:
    def longestKSubstr(self, s, k):
        left = 0
        max_len = -1
        freq = {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while len(freq) > k:
                freq[s[left]] -= 1

                if freq[s[left]] == 0:
                    del freq[s[left]]

                left += 1

            if len(freq) == k:
                max_len = max(max_len, right - left + 1)

        return max_len


'''
Pattern:
Variable Size Sliding Window

Key Observation:
The window size is not fixed.

We need the longest substring containing
exactly k distinct characters.

Expand the window until the number of
distinct characters exceeds k.

When that happens, shrink the window
from the left until the condition becomes
valid again.

Whenever the window contains exactly
k distinct characters, update the answer.

Approach:
1. Initialize left pointer and frequency map.
2. Expand the window using right pointer.
3. Add the current character to the map.
4. If distinct characters exceed k:
       - Shrink the window from the left.
       - Remove characters whose frequency
         becomes zero.
5. If the window contains exactly k
   distinct characters:
       - Update maximum length.
6. Return the longest valid length.

Time Complexity:
- O(n)

Each character enters and leaves the
window at most once.

Space Complexity:
- O(k)

Frequency map stores at most k distinct
characters.

Common Mistakes:
1. Updating max_len when distinct
   characters are less than k.

2. Forgetting to delete a character from
   the frequency map when its count
   becomes zero.

3. Using >= k inside the shrinking loop
   instead of > k.

4. Returning 0 instead of -1 when no
   valid substring exists.
'''