# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freq = defaultdict(int)
#         for num in nums:
#             freq[num] +=1
#         freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
#         return [item[0] for item in freq[:k]]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # print(count)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


        