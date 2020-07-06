class Solution:
    def validPalindrome(self, s):
        l=0
        r=len(s)-1
        n=0
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                n+=1
                if s[l+1]==s[r]:
                    l+=1
                elif s[l]==s[r-1]:
                    r-=1
                elif l==r-1 and n<1:
                    return True
                else:
                    print(n,l,s[0:l+3],len(s),r,s[len(s)-1:r-5:-1])
                    return False

        return n<=1
a=Solution()
print(a.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))