class Solution:
    def waysToChange(self, n):
        global res
        res=0
        coin=[1,5,10,25]

        def dfs(coin_val,start=0):

            for i in range(start,4):

                coin_val+=coin[i]

                if coin_val==n:
                    global res
                    res+=1
                elif coin_val<n:
                    dfs(coin_val,i)
                coin_val-=coin[i]

        dfs(0)

        return res

a=Solution()
# print(a.waysToChange(100))
for i in range(1,100):
    print(a.waysToChange(i),end=', ')
# class Solution1:
#     def waysToChange(self, n):
#         res=0
#         for a in range(n+1):
#             for b in range(n//5+1):
#                 for c in range(n//10+1):
#                     for d in range(n//25+1):
#                         if a+5*b+10*c+25*d==n:
#                             res+=1
#
#         return res
#
# b=Solution1()
# print(b.waysToChange(100))