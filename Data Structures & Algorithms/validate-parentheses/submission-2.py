class Solution:
    def isValid(self, s: str) -> bool:
        parensIn = "{[("
        parensOut = "]})"
        stack = []
        for paren in s:
            if paren in parensIn:
                stack.append(paren)
            else:
                if stack:
                    if not paren == "]" and stack[-1]=="[":
                        return False
                    elif not paren == "}" and stack[-1]=="{":
                        return False
                    elif not paren == ")" and stack[-1]=="(":
                        return False
                    else:
                        stack.pop(-1)
                else:
                    return False
        if stack:
            return False
        return True

        