class Solution(object):
    def minimumPairRemoval(self,nums):
        ops = 0

        while True:
            # Check if array is non-decreasing
            sorted_flag = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    sorted_flag = False
                    break

            if sorted_flag:
                return ops

            # Find adjacent pair with minimum sum
            min_sum = nums[0] + nums[1]
            idx = 0

            for i in range(1, len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            # Merge the pair
            nums[idx] = nums[idx] + nums[idx + 1]
            nums.pop(idx + 1)

            ops += 1

        