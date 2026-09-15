class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        LCS = 0
        numberSet = set(nums)
        
        
        for num in numberSet:
            if (num-1) not in numberSet:
                length = 1
                current = num

                while current+1 in numberSet:
                    current += 1
                    length += 1
                LCS = max(length, LCS)
        
        return LCS