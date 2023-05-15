'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.
'''
class Solution:
    def intToRoman(self, x: int) -> str:
        rn=""
        l1=x//1000
        if l1!=0:
            for i in range(l1):
                rn+="M"
        x=x-(l1*1000)
        if(x%1000>=900):
            rn+="CM"
            x=x-900
        #------------------------------------------------------
        l1=x//500
        if l1!=0:
            rn+="D"
        x=x-(l1*500)
        l1=x//100
        if l1!=0 and l1<4:
            for i in range(l1):
                rn+="C"
        if l1==4:
            rn+="CD"
        x=x-(l1*100)
        if(x%100>=90):
            rn+="XC"
            x=x-90
        #------------------------------------------------
        l1=x//50
        if l1!=0:
            rn+="L"
        x=x-(l1*50)
        l1=x//10
        if l1!=0 and l1<4:
            for i in range(l1):
                rn+="X"
        if l1==4:
            rn+="XL"
        x=x-(l1*10)
        if(x%10==9):
            rn+="IX"
            x=x-9
        #------------------------------------------------------
        l1=x//5
        if l1!=0:
            rn+="V"
        x=x-(l1*5)
        l1=x
        if l1!=0 and l1<4:
            for i in range(l1):
                rn+="I"
        if l1==4:
            rn+="IV"
        return rn
