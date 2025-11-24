class Solution(object):
    def prefixesDivBy5(self, nums):
        def check(bi):
            d=int(bi,2)
            if d%5==0:
                return True
            return False
        s=''
        for i in range(len(nums)):
            s+=str(nums[i])
            nums[i]=check(s)
        return nums
