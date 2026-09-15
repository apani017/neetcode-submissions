class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        t = ''
        for char in s:
            if char.isalnum():
                t+=char
        return t == t[::-1]
        