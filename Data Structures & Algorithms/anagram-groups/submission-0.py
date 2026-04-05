from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            key = tuple(sorted(i))
            d[key].append(i) 
        return list(d.values())