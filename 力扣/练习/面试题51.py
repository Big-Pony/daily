class Solution:
    def reversePairs(self, nums):
        def process(pop_index):
            pass
        res=0
        n=len(nums)
        index=[i for i in range(n)]

        lis=list(map(list,zip(nums,index)))
        lis.sort()
        for i in range(n):
            pass
        print(lis)
        lis=list(map(lambda x:[x[0],x[1]-1],lis))
        print(lis)


a=Solution()
a.reversePairs([7,5,6,4])
