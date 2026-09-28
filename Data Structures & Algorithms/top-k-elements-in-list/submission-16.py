class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            if len(heap) < k:
                heapq.heappush(heap, (count[num], num))
            else:
                heapq.heappushpop(heap, (count[num], num))
         
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res