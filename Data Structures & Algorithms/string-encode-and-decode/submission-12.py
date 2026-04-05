class Solution:

    def encode(self, strs: List[str]) -> str:
        a = [f'{len(i)}#{i}' for i in strs]
        return ''.join(map(str, a))

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i<len(s):
            j = s.index('#',i)
            length = int(s[i:j])

            word = s[j+1:length+j+1]
            result.append(word)
            i = length + 1 + j
        return result
