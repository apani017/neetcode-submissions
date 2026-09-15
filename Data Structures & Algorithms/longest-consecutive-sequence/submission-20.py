from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)

        print(numSet)
        longest = 0
        for num in numSet:
            if (num -1 ) not in numSet:
                streak = 1
                while (num + streak) in numSet:
                    streak+=1
                longest = max(longest, streak)
        return longest


        # keys = list(seq.keys())

        # longest = 1
        # streak = 1

        # for i in range(1, len(keys)):
        #     if keys[i] == keys[i - 1] + 1:
        #         streak += 1
        #         longest = max(longest, streak)
        #     else:
        #         streak = 1

        # return longest
