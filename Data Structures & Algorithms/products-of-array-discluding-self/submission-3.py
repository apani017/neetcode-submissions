import math
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)

        if zero_count > 1:
            return [0] * len(nums)

        product = 1
        for x in nums:
            if x != 0:
                product *= x

        res = [0] * len(nums)

        for i, num in enumerate(nums):
            if zero_count == 0:
                res[i] = product // num
            else:  # exactly one zero
                if num == 0:
                    res[i] = product
                else:
                    res[i] = 0

        return res
