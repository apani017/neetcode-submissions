from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seq = {}
        nums.sort()

        for num in nums:
            seq[num] = 1  # just need unique keys

        keys = list(seq.keys())

        longest = 1
        streak = 1

        for i in range(1, len(keys)):
            if keys[i] == keys[i - 1] + 1:
                streak += 1
                longest = max(longest, streak)
            else:
                streak = 1

        return longest
