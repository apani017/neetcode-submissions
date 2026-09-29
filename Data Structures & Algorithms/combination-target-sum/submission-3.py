class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def bt(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            curr.append(nums[i])
            bt(i, curr, total + nums[i])

            curr.pop()
            bt(i+1, curr, total)
        
        bt(0, [], 0)
        return res