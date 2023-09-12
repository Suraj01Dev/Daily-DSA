class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        back=set()
        for num in nums:
            if num in back:
                return True 
            else:
                back.add(num)
                
        return False

