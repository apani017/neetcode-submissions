class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []


        def bt():    
            if len(sub) == len(nums):
                res.append(sub.copy())

            for n in nums:
                if n not in sub:
                    sub.append(n)
                    bt()
                    sub.pop()
        bt()
        return res