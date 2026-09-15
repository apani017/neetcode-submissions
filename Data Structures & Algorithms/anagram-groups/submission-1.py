class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for index, word in enumerate(strs):
            sortedWord = "".join(sorted(word))
            res[sortedWord].append(word)
        # print([index, sortedWord])
        return list(res.values())
        