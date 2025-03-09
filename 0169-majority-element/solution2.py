class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # simpliest, sort the array, and take any from the right side, NlgN complexity 
        # if we dont to sort, we can count frequency with one-pass, and take the most frequent element with one pass (keep the largest) O(N) time and O(N) space 
        nums.sort()
        return nums[len(nums) // 2]
