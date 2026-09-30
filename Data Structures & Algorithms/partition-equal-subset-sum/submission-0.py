class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2

        n = len(nums)
        dp = {0}

        for i in range(len(nums)):
            newdp = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                
                newdp.add(t)
                newdp.add(t + nums[i])
            dp = newdp
        
        return False
                