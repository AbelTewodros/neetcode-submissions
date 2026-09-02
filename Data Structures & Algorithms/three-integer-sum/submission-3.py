class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        main = 0
        

        while main < len(nums)-2:
            left = main+1
            right = len(nums)-1
            target = nums[main]
            while left < right:
                curr =target+nums[left]+nums[right]
                if curr == 0:
                    sol.append([target,nums[left],nums[right]])
                    while right > left and nums[right] == nums[right-1]:
                        right -=1
                    while left < right and nums[left] == nums[left+1]: 
                        left+=1
                    right -=1
                    left -=1
                elif curr < 0:
                   left+=1
                else:
                   right -=1
            while main < len(nums)-2 and nums[main] == nums[main+1]:
                main+=1
            main+=1
        return sol
                    
