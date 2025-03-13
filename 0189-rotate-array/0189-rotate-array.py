class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums=len(nums)-1
        for i in range(k):
            new=nums.pop(len_nums)
            nums.insert(0,new)  
        return nums 


        