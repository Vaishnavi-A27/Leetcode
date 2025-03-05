class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        indx=len(nums)
        print(indx)
        for i in range(indx-1,-1,-1):
            if val== nums[i]:
                nums.pop(i)
            else:
                continue
        # print(type(nums))
        print(nums)
        
        