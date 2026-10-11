from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        for number in nums:
            if number != 0:
                nums[count] = number
                count += 1
        for index in range(count, len(nums)):
            nums[index] = 0

        print(nums)



slt = Solution()
slt.moveZeroes([1,2,3,4])
