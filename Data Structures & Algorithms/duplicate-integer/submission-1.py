class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        toggle = False
        n = len(nums)
        temp = []*n
        for i in range(n):
            if nums[i] in temp:
                toggle = True
                break
            else:
                temp.append(nums[i])
        return toggle
