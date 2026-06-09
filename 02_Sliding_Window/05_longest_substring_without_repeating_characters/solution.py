'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest
substring without repeating characters.

A substring is a contiguous sequence of characters.

Return the maximum length of such a substring.
'''

# ------------------------------------------------------------
# BRUTE FORCE APPROACH [O(n²)]
# ------------------------------------------------------------
'''
def lengthOfLongestSubstring_bruteforce(s):
    max_len = 0

    for i in range(len(s)):
        seen = set()

        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)

    return max_len


Approach:
1. Start a substring from every index.
2. Keep extending it to the right.
3. Store characters seen so far.
4. If a duplicate character appears:
       - Stop extending the substring.
5. Update the maximum valid length.
6. Return the longest valid length.

Time Complexity: O(n²)

Space Complexity: O(n)
'''
# ------------------------------------------------------------


# ------------------------------------------------------------
# OPTIMISED APPROACH [Variable Size Sliding Window]
# O(n)
# ------------------------------------------------------------

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        freq = {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            window_len = right - left + 1

            while window_len > len(freq):
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
                window_len = right - left + 1

            max_len = max(max_len, right - left + 1)

        return max_len


'''
Pattern:
Variable Size Sliding Window

Key Observation:
A valid window contains no repeating
characters.

If every character is unique:

window length == number of distinct characters

If a duplicate exists:

window length > number of distinct characters

Therefore, whenever:

window length > len(freq)

we know a duplicate character is present,
and we must shrink the window.

Approach:
1. Initialize left pointer and frequency map.
2. Expand the window using right pointer.
3. Add the current character to the map.
4. If a duplicate exists:
       - Shrink the window from the left.
       - Remove characters whose frequency
         becomes zero.
5. Update maximum window length.
6. Return the largest valid window.

Time Complexity:
- O(n)

Each character enters and leaves the
window at most once.

Space Complexity:
- O(n)

Frequency map stores characters currently
present in the window.

Common Mistakes:
1. Forgetting to remove a character from
   the frequency map when its count
   becomes zero.

2. Using 'if' instead of 'while' when
   shrinking the window.

3. Updating the answer before removing
   duplicate characters.

4. Confusing substring with subsequence.

5. Forgetting that the substring must be
   contiguous.
'''