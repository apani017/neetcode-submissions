# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         length = len(nums)
#         start = range(length)
#         for i in start:
#             for j in range(i+1, length):
#                 if nums[i] == nums[j]:
#                     return True
#         return False


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False