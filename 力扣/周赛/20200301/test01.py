class Solution:
    def smallerNumbersThanCurrent(self, nums):

        sn=nums[:]
        sn.sort()
        result=[sn.index(i) for i in nums]
        print(result)
        return result



a=Solution()
a.smallerNumbersThanCurrent([6,5,4,8])
a.smallerNumbersThanCurrent([7,7,7,7])
a.smallerNumbersThanCurrent([8,1,2,2,3])

