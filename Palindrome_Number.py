'''
Given an integer x, return true if x is a palindrome, and false otherwise.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            t=x
            p=0
            while t>0:
                p=p*10+(t%10)
                t=t//10
            if(p!=x):
                return False
            else:
                return True
            
                
