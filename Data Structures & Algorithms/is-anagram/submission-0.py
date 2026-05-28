class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ok = sorted(s) == sorted(t)

        return ok
        