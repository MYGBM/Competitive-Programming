class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        so=sorted(nums)
        output=[]
        for i in range(len(nums)):
            if target==so[i]:
                output+=[i]
        return output
