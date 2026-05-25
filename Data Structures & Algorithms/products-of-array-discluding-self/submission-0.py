class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []

        prefix = 1
        for i, num in enumerate(nums):
            results.append(prefix)
            prefix *= num

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            results[i] *= suffix
            suffix *= nums[i]

        return results