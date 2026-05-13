from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_min = float("inf")
        second_min = float("inf")
        for value in nums: #1
            if value <= first_min:
                first_min = value
            elif value <= second_min:
                second_min = value
            else:
                return True


        return  False


slt = Solution()
print(slt.increasingTriplet([2,1,5,0,4,6]))
