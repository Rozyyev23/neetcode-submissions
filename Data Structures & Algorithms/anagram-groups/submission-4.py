class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for i in strs:
            k = tuple(sorted(i))
            d[k].append(i)
        return list(d.values())