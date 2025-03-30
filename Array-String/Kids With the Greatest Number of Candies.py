    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxi = max(candies)
        for i in candies:
            if i + extraCandies >= maxi:
                result.append(True)
            else :
                result.append(False)
        return result
