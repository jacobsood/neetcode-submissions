class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort() # O(n log n) - TimSort

        maximum = 0
        consecutive = 1
        last = nums[0]

        for num in nums:
            if num == last + 1:
                consecutive += 1
            elif num != last:
                consecutive = 1
            
            last = num
            maximum = max(maximum, consecutive)

        return maximum