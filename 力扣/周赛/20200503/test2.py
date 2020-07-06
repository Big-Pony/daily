class Solution:
    def kLengthApart(self, nums, k):
        n=len(nums)
        his=[]
        for i in range(n):
            if nums[i]==1:
                his.append(i)
        for i in range(1,len(his)):
            if his[i]-his[i-1]-1<k:
                return False
        return True

a=Solution()
print(a.kLengthApart(nums = [1,0,0,0,1,0,0,1], k = 2))
print(a.kLengthApart([1,0,0,1,0,1],2))