# 605. Can Place Flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0) 
        flowerbed.insert(0, 0)
        i=1
        while i<len(flowerbed)-1:
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i]=1
                n-=1
            i +=1
        return n <= 0
        