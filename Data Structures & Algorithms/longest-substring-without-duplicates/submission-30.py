class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        max_k = 0
        j = 0
        left = 0

        for i in range(len(s)):
            while s[i] in st:
                st.remove(s[left])
                left += 1
            st.add(s[i])
            j = i - left + 1
            max_k = max(max_k, j)
        return max_k
            