class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # [-4, -1, -1, 0, 1, 2]
        # num[i] = - (nums[j] +  nums[k])
        res = []
        for i in range(len(nums)):
            target = -nums[i]
            j, k = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j<k:
                twoSum = nums[j] + nums[k]
                if twoSum < target:
                    j+=1
                elif twoSum > target:
                    k-=1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    # Skip duplicates for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # Skip duplicates for k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                



        return res