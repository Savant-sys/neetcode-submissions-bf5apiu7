class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums 
            
        answer = [] 
        
        for i in range(len(nums)):
            
            element = 1 
            for j in range(len(nums)): 
                if i != j: 
                    element *= nums[j] 
                
            answer.append(element) 
            
        return answer