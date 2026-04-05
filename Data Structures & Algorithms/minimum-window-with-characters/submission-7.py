from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        s_count = Counter()
        left, have = 0, 0
        need = len(t_count)
        len_res = float('inf')
        res = [-1, -1]
        for r in range(len(s)):

            s_count[s[r]] += 1

            if s_count[s[r]] == t_count[s[r]]:
                have += 1
            
            while have == need:
                if r - left + 1 < len_res:
                    len_res = r - left + 1
                    res = [left, r]
                s_count[s[left]] -= 1
                
                if s_count[s[left]] < t_count[s[left]]:
                    have -= 1

                left += 1
        return s[res[0]:res[1]+1]