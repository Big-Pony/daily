class Solution:
    def longestPalindrome(self, s):
        n=len(s)
        max_str=''
        for i in range(n):
            for j in range(i+1,n):
                sonstr=s[i:j+1]
                if sonstr==sonstr[-1::-1]:
                    if len(sonstr)>len(max_str):
                        max_str=sonstr

        return max_str


a=Solution()

print(a.longestPalindrome("babad"))
print(a.longestPalindrome("cbbd"))

