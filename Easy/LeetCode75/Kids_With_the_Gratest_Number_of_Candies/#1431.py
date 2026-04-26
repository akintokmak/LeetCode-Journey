class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        maxCandies = max(candies)
        for candie in candies:
            is_greatest =  (candie + extraCandies) >= maxCandies
            result.append(is_greatest)
        return result


slt = Solution()
print(slt.kidsWithCandies([4,2,1,1,2],1))



