class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_l = 1
        left = [1] * len(nums)

        prefix_r = 1
        right = [1] * len(nums)

        for i in range(len(nums)):
            left[i] = prefix_l
            prefix_l *= nums[i]

        for j in range(len(nums)-1,-1,-1):
            right[j] = prefix_r
            prefix_r *= nums[j]

        return [right[i] * left[i] for i in range(len(nums))]
