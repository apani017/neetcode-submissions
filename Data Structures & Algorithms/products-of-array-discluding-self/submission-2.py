# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         size = len(nums)
#         res = [0] * size
        
#         for i in range(size):
#             prod = 1
#             for j in range(size):
#                 if i == j:
#                     continue
#                 prod *= nums[j]
            
#             res[i] = prod
#         return res

# [1,2,4,6]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n-1] = 1

        for i in range(1,n):
            pref[i] = nums[i-1]*pref[i-1]

        for i in range(n-2, -1, -1):
            suff[i] = nums[i+1] * suff[i+1]

        for i in range(n):
            res[i] = pref[i]*suff[i]

        return res

