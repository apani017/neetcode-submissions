class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums = nums
        nums_set = set()
        
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False
        # return len(nums_set) != len(nums)