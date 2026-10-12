class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set() 
        #when duplicate or "have I seen this before?" think of a set
        for i in nums:
            if i in seen:
                return True 
            seen.add(i)
        return False  
        

    
        