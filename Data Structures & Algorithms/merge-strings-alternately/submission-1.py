class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, res = 0, ""
        while i < len(word1):
            if i < len(word2):
                res += word1[i] + word2[i]
            else:
                res += word1[i:len(word1)]
                return res
            i += 1
            if i == len(word1):
                res += word2[i:len(word2)]
                return res
        return res