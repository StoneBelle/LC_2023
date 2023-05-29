class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        
        p = 0 
        length = len(flowerbed)

        for f in range(length - 1)[::2]:
            if f < length - 1:
                if flowerbed[f] == flowerbed[f + 1]:
                    p += 1
        if flowerbed[length - 1] != 1 and flowerbed[length-2] != 1:
                p += 1 
        return n <= p
