import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+":operator.add, "*":operator.mul, "-":operator.sub, "/":operator.truediv}
        stack = []
        for token in tokens:
            if not token in operators:
                stack.append(int(token))
            else:
                b = stack.pop(-1)
                a = stack.pop(-1)
                stack.append(int(operators[token](a,b)))
        return stack[-1]
            

        