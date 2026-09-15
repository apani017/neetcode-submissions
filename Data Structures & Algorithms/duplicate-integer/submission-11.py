class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        start = range(length)
        for i in start:
            for j in range(i+1, length):
                if nums[i] == nums[j]:
                    return True
        return False
