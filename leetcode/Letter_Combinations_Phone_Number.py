17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def rec_f(st, digits):
            if len(digits) == 0:
                output.append(st)
            else:
                for letter in phone[digits[0]]:
                    rec_f(st+letter, digits[1:])
        output=[]
        if digits:
            rec_f("", digits)
        return output    