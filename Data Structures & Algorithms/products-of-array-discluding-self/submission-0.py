class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pref = [1 for i in range(length)]
        suff = [1 for i in range(length)]
        for i in range(1, length):
            pref[i] = pref[i - 1] * nums[i - 1]
        for i in range(length - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]
        for i in range(length):
            pref[i] *= suff[i]
        return pref

            


# [1,2,4,6]
# pref = [1, 1, 2, 8]
# suff = [48, 24, 6, 1]
# out = [48, 24, 12, 8]