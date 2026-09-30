class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsHash = {}
        for i in range(len(nums)):
            if (target - nums[i]) in numsHash.keys():
                return [numsHash[target - nums[i]], i]
            if (nums[i] not in numsHash.keys()):
                numsHash[nums[i]] = i