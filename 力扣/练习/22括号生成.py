class Solution:
    def generateParenthesis(self, n):
        def match(s):
            left=0
            for i in s:
                if i=='(':
                    left+=1
                else:
                    if left<1:
                        return False
                    left-=1

            return left==0
        def all_kh(lis):
            if len(lis)==2*n:
                if match(lis):

                    res.append(''.join(lis[:]))
            else:
                lis.append('(')
                all_kh(lis)
                lis.pop()
                lis.append(")")
                all_kh(lis)
                lis.pop()


        res=[]
        all_kh([])
        return res


a=Solution()

print(a.generateParenthesis(6))


