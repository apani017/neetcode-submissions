# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower().replace(" ", "")
#         t = ''
#         for char in s:
#             if char.isalnum():
#                 t+=char
#         return t == t[::-1]


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = "".join(filter(str.isalnum, s)).lower()
#         n = len(s)

#         # if n//2 == 0:
#         print(n)
#         print(s[:n//2], s[:n//2-1:-1])

#         if n % 2 == 0:
#             return s[:n//2] == s[:n//2-1:-1]
#         else:
#             return s[:n//2] == s[:n//2:-1]

### n = 4, 0=3, 1=2
### n = 5, 0=4, 1=3

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not str.isalnum(s[l]):
                l+=1
            while r>l and not str.isalnum(s[r]):
                r-=1
            if s[l]!=s[r]:
                return False
            l,r = l+1, r-1
        return True