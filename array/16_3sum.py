class Solution:
    def twoSum(self, nums, target, i, j, res):
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                # skip duplicates
                while i < j and nums[i] == nums[i + 1]:
                    i += 1
                while i < j and nums[j] == nums[j - 1]:
                    j -= 1

                res.append([-target, nums[i], nums[j]])
                i += 1
                j -= 1

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []

        # sort
        nums.sort()
        n = len(nums)

        # fixing n1
        for i in range(0, n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            n1 = nums[i]
            target = -n1
            self.twoSum(nums, target, i + 1, len(nums) - 1, res)

        return res
