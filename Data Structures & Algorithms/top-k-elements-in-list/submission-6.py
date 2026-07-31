class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencyMap = {}
        for num in nums:
            frequencyMap[num] = frequencyMap.get(num, 0) + 1
            
        list_arr = [] 
        for num, freq in frequencyMap.items():
            list_arr.append([freq, num])
        list_arr.sort()


        result = []
       
        for i in range(k):
            result.append(list_arr.pop()[1])
        return result
