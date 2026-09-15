class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        LCS = 0
        mySet = set(nums)

        for num in mySet:
            if num - 1 not in mySet:
                current = num
                length = 1
            
                while current + 1 in mySet:
                    current+=1
                    length+=1
                LCS = max(length, LCS)
        return LCS