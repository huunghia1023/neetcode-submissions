class Solution:
    def validPalindrome(self, s: str) -> bool:
        # s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])

            l += 1
            r -= 1

        return True