class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        comp = strs[1:]
        print(comp)
        for i in range(len(strs[0])):
            for s in comp:
                if i == len(s) or strs[0][i] != s[i]:
                    return res
                
            res += strs[0][i]
        return res