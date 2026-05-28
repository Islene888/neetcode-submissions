class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        length = 0
        left = 0
        for right in range(len(s)):
            while s[right] in s_set:
                s_set.remove(s[left])
                left += 1

            length = max(length,right - left +1)
            s_set.add(s[right])
        return length


        