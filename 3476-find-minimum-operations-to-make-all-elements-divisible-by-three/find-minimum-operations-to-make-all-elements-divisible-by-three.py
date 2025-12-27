class Solution(object):
    def minimumOperations(self, nums):
        steps=0
        for i in nums:
            t=i%3
            if t!=0:
                steps+=min(t,3-t)
        return steps
        