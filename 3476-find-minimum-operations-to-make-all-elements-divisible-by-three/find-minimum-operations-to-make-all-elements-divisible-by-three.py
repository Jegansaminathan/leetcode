class Solution(object):
    def minimumOperations(self, nums):
        steps=0
        for i in nums:
            if(i%3!=0):
                steps+=1
        return steps
        