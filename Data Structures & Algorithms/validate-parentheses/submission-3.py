class Solution:
    def isValid(self, s: str) -> bool:
        parensDict = {"]":"[", "}":"{", ")":"("}
        stack = []
        for paren in s:
            if paren not in parensDict:
                stack.append(paren)
            else:
                if stack:
                    if not parensDict[paren]==stack[-1]:
                        return False
                    else:
                        stack.pop(-1)
                else:
                    return False
        if stack:
            return False
        return True

        