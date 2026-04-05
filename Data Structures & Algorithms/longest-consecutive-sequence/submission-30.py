class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        nums = set(nums)
        if len(nums) == 0:
            return 0
        for i in nums:
            if i-1 not in nums:
                length = 1
                while i+length in nums:
                    length +=1
                max_length = max(length, max_length)
        return max_length