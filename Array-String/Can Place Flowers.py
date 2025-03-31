def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    counter = 0
    if n == 0:
        return True
    if len(flowerbed) == 1:
        return True if flowerbed[0] == 0 and n == 1 else False
    if flowerbed[0] == 0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        counter += 1
    if flowerbed[-1] == 0 and flowerbed[-2] == 0:
        flowerbed[-1] = 1
        counter += 1
    for i in range(1, len(flowerbed) - 1):
        x, y, z = flowerbed[i-1], flowerbed[i], flowerbed[i+1]
        if x == 0 and y == 0 and z == 0:
            flowerbed[i] = 1
            counter +=1
    if counter >= n:
        return True
    else:
        return False
