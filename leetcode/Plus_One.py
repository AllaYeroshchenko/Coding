# 66. Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        new_dig=digits[n-1]+1
        if new_dig <= 9:
            digits[n-1] = new_dig
            return digits
        else:
            digits[n-1] = 0
            i=n-2
            while digits[i] == 9:
                digits[i]=0
                i-=1
            if i>=0:
                digits[i]+=1
            else:
                digits.insert(0, 1)
        return digits            