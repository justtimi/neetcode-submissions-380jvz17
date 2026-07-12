class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            current_number = nums[i]
            number_needed = target - nums[i]

            if(number_needed in seen):
                return [seen[number_needed], i]
            
            seen[current_number] = i
            
        