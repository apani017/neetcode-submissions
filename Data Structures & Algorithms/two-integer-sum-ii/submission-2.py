class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # nums[i] + nums[j] = target # i != j
        # diff = target - nums[i]

        hashmap = {} # val -> index
        for i, val in enumerate(numbers):
            diff = target - val

            if diff in hashmap:
                return [hashmap[diff], i+1]
            hashmap[val] = i+1
        