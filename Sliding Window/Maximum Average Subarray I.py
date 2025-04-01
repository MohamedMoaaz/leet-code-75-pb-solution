def findMaxAverage(self, nums: List[int], k: int) -> float:
    
    window_sum = sum(nums[:k])
    maximum_avg = window_sum / k

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        maximum_avg = max(maximum_avg, window_sum / k)

    return maximum_avg
