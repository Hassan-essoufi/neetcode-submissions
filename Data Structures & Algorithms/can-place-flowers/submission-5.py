class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        p = 0
        if len(flowerbed) == 1:
            return True if (flowerbed[0] == 0 and n ==1) or n==0 else False
        if flowerbed[:2] == [0,0]:
            p +=1
        if flowerbed[-3:] == [0,0]:
            p +=1
        for i in range(1,len(flowerbed)):
            if flowerbed[i-1: i+2] == [0,0,0]:
                p += 1
                flowerbed[i] = 1
        return True if p >= n else False