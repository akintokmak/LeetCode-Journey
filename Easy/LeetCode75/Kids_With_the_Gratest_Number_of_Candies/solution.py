class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        maxCandies = max(candies)

        for candie in candies:
            result.append((candie + extraCandies) >= maxCandies)
        return result