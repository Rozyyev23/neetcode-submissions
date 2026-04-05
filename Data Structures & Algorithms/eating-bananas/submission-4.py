class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k):
            """Может ли Кико съесть все за h часов со скоростью k?"""
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k  # ceil division
            return hours <= h
        
        # Binary search на K
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid  # может быть еще медленнее
            else:
                left = mid + 1  # нужно быстрее
        
        return left