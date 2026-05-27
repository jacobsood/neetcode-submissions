class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maximum = 0

        for num in seen:
            if num - 1 not in seen:  # only start sequences here
                length = 1
                while num + length in seen:
                    length += 1
                maximum = max(maximum, length)

        return maximum