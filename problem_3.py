class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = end = 0
        max_len_substring = 0
        substring = set()
        while end < len(s):
            if s[end] in substring:
                while s[end] in substring:
                    substring.remove(s[start])
                    start += 1
            else:
                substring.add(s[end])
                max_len_substring = max(max_len_substring, len(substring))
                end += 1
        return max_len_substring