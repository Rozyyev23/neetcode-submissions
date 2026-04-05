class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicti = {}
        for i in nums:
            if i in dicti:
                return True
            dicti[i] = True
        return False