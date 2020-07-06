class Solution:
    def reverseWords(self, s):
        s=s.strip(' ')
        zifu=[]
        left=0
        right=0
        n=len(s)
        while left<n and right<n:
            while s[left]==' ':
                left+=1
                if left>=n-1:
                    break
            right=left

            while right<n and s[right]!=' ':
                right+=1


            zifu.append(s[left:right])
            left=right+1
        res=' '.join(zifu[i] for i in range(len(zifu)-1,-1,-1))
        print(res)
        return res

a=Solution()
a.reverseWords("the sky is blue")
a.reverseWords("  hello world!  ")
a.reverseWords("a good   example")
