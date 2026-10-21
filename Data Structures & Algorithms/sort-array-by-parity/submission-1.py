class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            while (nums[i] % 2 == 1 and i < j):
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j -= 1
            i += 1
        return nums
# [1, 3, 5, 7, 9]