from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(dict(sorted(Counter(nums).items(), key = lambda item:item[1], reverse=True)).keys())[:k]
  