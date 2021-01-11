# 680. Valid Palindrome II

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, n =0, len(s)
        while i <= (n-1)//2:
            if s[i] == s[n-i-1]:
                i+=1
            else:
                if s[:i]+s[i+1:] == (s[:i]+s[i+1:])[::-1]:
                    return True
                elif s[:n-i-1]+s[n-i:] == (s[:n-i-1]+s[n-i:])[::-1]:
                    return True
                else:
                    return False
        return True        
