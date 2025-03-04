class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mindx=m+n-1
        nindx=n-1

        nums1_len=len(nums1)
        for i in range (nums1_len ):
            if nums1[mindx]==0:
                nums1[mindx]=nums2[nindx]
                mindx-=1
                nindx-=1
                if mindx==-1 or nindx==-1:
                    break
        
        nums1.sort()
        return nums1

        
        
        