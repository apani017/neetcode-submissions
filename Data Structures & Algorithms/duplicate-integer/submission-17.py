class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = nums
        nums_set = set(nums)
        # print(nums_set)
        # print(len(nums_set) == len(nums))
        return len(nums_set) != len(nums)