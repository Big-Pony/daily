class Solution:
    def longestPrefix(self, s):
        n=len(s)

        right=n-1

        max_l = 0

        for i in range(n-1):
            if s[:i+1]==s[right:]:
                max_l=i+1
            right-=1

        return s[:max_l]
a=Solution()

print(a.longestPrefix("level"))
print(a.longestPrefix("leetcodeleet"))