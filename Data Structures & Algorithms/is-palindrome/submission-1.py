class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ''
        for c in s:
            if c.isalnum():
                tmp+=c.lower()
        n = len(tmp)
        left = 0
        right = n-1
        while left<right:
            if tmp[left] != tmp[right]:
                return False
            left += 1
            right -= 1
        return True
        
        