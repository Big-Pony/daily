class Solution:
    def longestSubarray(self, nums,limit):
        n=len(nums)
        dp=[]
        for i in range(n):

            for j in range(i,n):
                if nums[j]-nums[i]<=limit:
                    pass
                else:
                    break