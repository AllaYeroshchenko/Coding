# 14. Longest Common Prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref=""
        if len(strs) == 0:
            return pref
        min_length = min([len(x) for x in strs])
        if min_length==0:
            return pref
        i=1
        letter=""
        while i<=min_length:
            letter=letter+strs[0][i-1]
            for word in strs:
                if letter != word[:i]:
                    return pref
            i+=1
            pref=letter         
        return pref             
        