class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            m = (l + r) // 2
            
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l
        # print(f"l={l},r={r}")
        def bs(l, r) -> int:
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        res = bs(0, pivot - 1)
        return res if res != -1 else bs(pivot, len(nums)-1)
