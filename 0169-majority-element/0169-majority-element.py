from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occour=Counter(nums)
        max_occour=max(occour)
        return max_occour




        