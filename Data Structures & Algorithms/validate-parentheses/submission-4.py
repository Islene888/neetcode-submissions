class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ']':'[',
            '}':'{',
            ')':'('
        }
        if len(s)%2 ==1:
            return False
        for c in s:
            if c in mapping:
                if not stack or mapping[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
        