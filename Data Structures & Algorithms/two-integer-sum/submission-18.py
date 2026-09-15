# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(0, len(nums)):
#             for j in range(i+1, len(nums)):
#                 if(nums[i] + nums[j] == target): return [i, j]
#         return []


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for key, val in enumerate(nums):
            # indices[val] = key

            diff = target - val
            if diff in indices:
                return [indices[diff], key]
            indices[val] = key
        # print(indices)

