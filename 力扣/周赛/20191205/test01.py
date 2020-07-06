
class Solution:
    def getDecimalValue(self, head):
        sum_ = 0
        for i in range(-1,-len(head)-1,-1):

            if head[i]==1:
                k=-i-1
                sum_+=2**k
        print('sum',sum_)

a=Solution()
a.getDecimalValue( head = [0])