class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = (l + r) // 2
            
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
        
        minI = r
        if minI == 0:
            l, r = 0, len(nums) - 1
        elif nums[0] <= target <= nums[minI-1]:
            l, r = 0, minI - 1
        else:
            l, r = minI, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1



        