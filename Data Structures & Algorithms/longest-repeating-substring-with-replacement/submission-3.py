class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        left = 0
        max_freq = 0
        
        for right in range(len(s)):
            # Добавляем символ в словарь
            char = s[right]
            count[char] = count.get(char, 0) + 1
            
            # Обновляем max_freq
            max_freq = max(max_freq, count[char])
            
            # Если окно невалидно, сдвигаем левую границу
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                
            # Обновляем результат
            res = max(res, right - left + 1)
            
        return res