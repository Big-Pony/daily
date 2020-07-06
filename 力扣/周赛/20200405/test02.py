class Solution:
    def numSteps(self, s):
        import math
        def two_to_ten(s):
            n=len(s)
            res=0
            for i in range(n):
                if s[i]=='1':
                    res+=2**(n-i-1)
            return res

        s = two_to_ten(s)
        i=0

        while s!=1:
            i+=1

            if s%2==0:

                s=s//2
            else:
                s+=1



        return i
a=Solution()

#print(a.numSteps('1101'))
#print(a.numSteps('10'))
#print(a.numSteps('1'))
print(a.numSteps("1111011110000011100000110001011011110010111001010111110001"))
