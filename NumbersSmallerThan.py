class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        new=[0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    new[i]+=1
        return(new)
