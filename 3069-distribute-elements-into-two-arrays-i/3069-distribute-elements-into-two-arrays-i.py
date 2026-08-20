class Solution:
    def resultArray(self, nums):
        self.arr1 = []
        self.arr2 = []
        self.arr1.append(nums[0])
        self.arr2.append(nums[1])
        for i in range(2, len(nums)):
            if self.arr1[-1] > self.arr2[-1]:
                self.arr1.append(nums[i])
            else:
                self.arr2.append(nums[i])
        return self.arr1 + self.arr2
nums = [2, 1, 3]
oparation = Solution()
oparation.resultArray(nums)