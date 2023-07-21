'''
3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105
'''

#This code uses a two pointer approach
#We first sort the list and then we narrow down the window from both ends instead of traversing the entire list over and over again.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            
            j=i+1
            k=len(nums)-1

            while j<k:
                s=nums[i]+nums[j]+nums[k]

                if s>0:
                    k-=1
                elif s<0:
                    j+=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1       
                  #This while loop is just to avoid duplicates.
                  # More efficient than having to form more triplets than necessary and checking if they already exist
                    while nums[j-1]==nums[j] and j<k:               
                        j+=1
        return ans
