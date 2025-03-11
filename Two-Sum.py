class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[i] + nums[i+1]
        \\\num_set = set()
        for i,n in enumerate(nums):
            difference = target - n

            if difference in num_set:
                return [nums.index(difference),i]
            num_set.add(n)
        return []
        \\\
        for i in range(0,len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]