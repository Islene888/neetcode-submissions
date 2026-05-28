class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        self.length = []
        for s in strs:
            res = res + s
            self.length.append(len(s))
        return res

    def decode(self, s: str) -> List[str]:
        tmp = 0
        res = []
        for num in self.length:
            res.append(s[tmp:(tmp+num)])
            tmp += num
        return res




