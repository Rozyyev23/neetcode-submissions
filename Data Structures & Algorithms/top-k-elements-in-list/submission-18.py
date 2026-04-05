from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict(sorted(Counter(nums).most_common(k), key = lambda num: num[0]))
        return list(d.keys())