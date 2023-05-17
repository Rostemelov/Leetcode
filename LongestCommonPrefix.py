'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        mini=999
        if(len(strs)==1):
            return strs[0]
        for i in strs:
            n1=len(i)
            mini=min(n1,mini)

        for i in range(0,mini):
            p=strs[0][i]
            for j in strs:
                if j[i]!=p:
                    return prefix
            prefix+=p
        return prefix
        
