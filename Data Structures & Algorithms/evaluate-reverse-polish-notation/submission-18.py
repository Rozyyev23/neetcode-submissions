class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        sum = []
        sum_n = 0

        for i in range(len(tokens)):
            if tokens[i] not in  ['+','-','*','/']:
                sum.append(int(tokens[i]))
            elif tokens[i] == '+':
                a = sum.pop()
                b = sum.pop()
                sum.append(a + b)
            elif tokens[i] == '-':
                a = sum.pop()
                b = sum.pop()
                sum.append(b - a)
            elif tokens[i] == '*':
                a = sum.pop()
                b = sum.pop()
                sum.append(a * b)
            elif tokens[i] ==  '/':
                a = sum.pop()
                b = sum.pop()
                sum.append(int(b / a))

        return sum[-1]



        