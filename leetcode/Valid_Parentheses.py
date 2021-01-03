# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        brackets={"(": ")", "{": "}", "[": "]"}
        expected=[]
        for ch in s:
            if ch in brackets.keys():
                expected.append(brackets[ch])
            if ch in brackets.values():
                if len(expected)==0 or ch not in expected:
                    return False
                if expected[-1]==ch:
                    expected.pop()
        if len(expected)==0:
            return True
        else:
            return False
        