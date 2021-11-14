#psuedo code
#Take one element
#Add this element with every other element
#After adding, compare the sum with the given target
#If the sum is equal to the target, return the indices of these two elements
#If the sum is not equal to the target, we check for the next pair

def twoSum(self, nums, target):
    #for every i in the range 0 to (length of the number-1) [Take one element]
    for i in range(0, len(nums)-1):
        # for every j in the range of i+1 (Add this element with every other element)
        for j in range(i+1, len(nums)):
            #If the sum is equal to the target, return the indices of these two elements
            if (nums[i] + nums[j] == target):
                return [i,j]


#O(N^2) runtime
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
