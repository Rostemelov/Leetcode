/*
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
*/

class Solution {

    int top=-1;
    char c[]=new char[10000];

    void push(char sp)
    {
        top++;
        c[top]=sp;
    }
    void pop()
    {
        top--;
    }

    public boolean isValid(String s) {

    int len=s.length();
    char ch[]=s.toCharArray();
    for(int i=0;i<len;i++)
    {
        if(ch[i]=='(' || ch[i]=='[' || ch[i]=='{')
        {
            push(ch[i]);
        }
        else if(ch[i]==')' || ch[i]==']' || ch[i]=='}')
        {
            if(top<0){return false;}
            else if(ch[i]==')' && c[top]=='('){pop();}
            else if(ch[i]==']' && c[top]=='['){pop();}
            else if(ch[i]=='}' && c[top]=='{'){pop();}
            else{return false;}
        }
    }
    if(top==-1){return true;}
    else{return false;}      
    }
}
