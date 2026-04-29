from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.insert(0,0)
        flowerbed.append(0)
        count = 0
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1] + flowerbed[i] + flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count += 1
        return count >= n


slt = Solution()
print(slt.canPlaceFlowers(flowerbed=[1,0,0,0,1],n=1))