class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = []
        if len(nums) == 0:
            return 0
        nums = set(nums)
        for i in nums:
            if i-1 not in nums:
                length = 1
                while i+length in nums:
                    length +=1
                s.append(length)
        return max(s)