'''
Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"


Constraints:

    1 <= num1.length, num2.length <= 200
    num1 and num2 consist of digits only.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.
'''

class Solution:

    def strtoint(self, num:str)->int:
        x=0
        d={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0,}
        for i in range(len(num)):
            x=x*10+d[num[i]]
        return x

    def multiply(self, num1: str, num2: str) -> str:
        x=0
        y=0
        l=len(num1)
        m=len(num2)
        x=self.strtoint(num1)
        y=self.strtoint(num2)
        z=str(x*y)
        return str(z)
