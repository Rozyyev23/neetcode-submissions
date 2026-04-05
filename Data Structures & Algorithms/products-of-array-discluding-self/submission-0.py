class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_l = 1
        left = [1] * len(nums)
        prefix_r = 1
        right = [1] * len(nums)
        for i in range(len(nums)):
            left[i] = prefix_l
            prefix_l *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            right[i] = prefix_r
            prefix_r *= nums[i]
        return [left[i] * right[i] for i in range(len(nums))]
