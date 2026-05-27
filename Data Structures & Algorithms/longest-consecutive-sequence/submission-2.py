class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maximum = 0
        seen: dict[int, tuple[int, int]] = {}

        for num in nums:
            if num - 1 in seen and num + 1 in seen:
                low, _ = seen[num - 1]
                _, high = seen[num + 1]
                seen[num] = (low, high)
                seen[low] = (low, high)
                seen[high] = (low, high)
                maximum = max(maximum, high - low + 1)

            elif num - 1 in seen:
                low, _ = seen[num - 1]
                seen[low] = (low, num)
                seen[num] = (low, num)
                maximum = max(maximum, num - low + 1)

            elif num + 1 in seen:
                _, high = seen[num + 1]
                seen[high] = (num, high)
                seen[num] = (num, high)
                maximum = max(maximum, high - num + 1)

            else:
                seen[num] = (num, num)
                maximum = max(maximum, 1)

        return maximum