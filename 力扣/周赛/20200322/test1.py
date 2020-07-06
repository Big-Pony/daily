class Solution:
    def createTargetArray(self, nums, index):
        n=len(nums)
        result=[]
        for i in range(n):
            if index[i]==len(result):
                result.append(nums[i])
            else:
                result.insert(index[i],nums[i])
        # result='{}'.format(nums[0])
        # print(result)
        # for i in range(1,n):
        #     if index[i]<len(result):
        #         result=result[0:index[i]]+str(nums[i])+result[index[i]:]
        #     else:
        #         result+=str(nums[i])
        # result=[int(i) for i in result]
        # return result
        return result

a=Solution()
print(a.createTargetArray([0,1,2,3,4],[0,1,2,2,1]))
print(a.createTargetArray([1],[0]))
print(a.createTargetArray([5,11,1,1,15,13,17,10,11,7,13,9,1,14,8,12,12,10,10]\
                          ,[0,0,2,1,3,0,2,1,6,8,2,4,4,1,5,3,11,4,7]))