class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = -1
        n = len(nums)
        mid = n//2
        
        if nums[mid] > target:
            for i in range(0, mid):
                if nums[i] == target:
                    index = i
        else:
            for i in range(mid, n):
                if nums[i] == target:
                    index = i

        return index
        