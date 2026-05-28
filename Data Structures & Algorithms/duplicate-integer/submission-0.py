class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1 = set(nums)
        a = len(nums1)
        b = len(nums)
        if a == b:
            return False
        else:
            return True
        