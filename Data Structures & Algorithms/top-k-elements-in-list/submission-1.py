from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        most_frequent = frequency.most_common(k)
        return [number for number, count in Counter(nums).most_common(k)]