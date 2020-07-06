class Solution:
    def longestDiverseString(self, a, b, c):
        res=''
        def judge(zge,zgest,j,jst,y,yst,res,n,condition):

            if n > 2:
                if res[-1] == zgest and res[-2] == zgest:
                    if max(j, y) > 0:
                        if max(j, y) == j:
                            res += jst
                            j -= 1
                        else:
                            res += yst
                            y -= 1
                    else:
                        condition=1
                else:
                    res += zgest
                    zge -= 1
            else:
                res += zgest
                zge -= 1
            return zge,j,y,res,n,condition
        while max(a,b,c)>0:
            n=len(res)
            
            condition = 0
            if max(a,b,c)==a:

                a,b,c,res,n,condition=judge(a,"a",b,"b",c,"c",res,n,condition)
                if condition==False:
                    break


            elif max(a,b,c)==b:

                b,a,c,res,n,condition =judge(b, "b", a, "a", c, "c", res, n,condition)
                if condition==False:
                    break


            else:
                c,b,a,res,n,condition= judge(c, "c", b, "b", a, "b", res, n,condition)
                if condition==False:
                    break
        return res
a=Solution()

print(a.longestDiverseString(a = 1, b = 1, c = 7))