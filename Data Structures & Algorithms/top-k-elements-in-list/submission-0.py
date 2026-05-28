from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = list(Counter(nums).items())
        counter.sort(key=lambda x:x[1],reverse = True)
        res = []
        count = 0
        for key,val in counter:
            if count < k:
                res.append(key)
                count += 1
        return res

        