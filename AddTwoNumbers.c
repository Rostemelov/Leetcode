/*
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes 
contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

 

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.


*/


//Approach1: Accept and send back as linked list- my code. solved 1138 out 1568 cases.
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){

struct ListNode* temp1=l1;
struct ListNode* temp2=l2;
struct ListNode* tt;
struct ListNode* last;
int carry=0;
int sum;

while(temp1!=NULL && temp2!=NULL)
{
    if(temp2==NULL)
    {break;}
    if(temp1->next==NULL){last=temp1;}
    if(temp1==NULL)
    {
        last->next=temp2;
        last->val=(last->val+carry)%10;
        carry=(last->val+carry)/10;
        tt=temp2;
        temp1=last->next;
        temp2=temp2->next;
        free(tt);
        continue;
    }
    sum=(temp1->val+temp2->val+carry)%10;
    carry=(temp1->val+temp2->val+carry)/10;
    temp1->val=sum;
    tt=temp2;
    temp1=temp1->next;
    temp2=temp2->next;
    free(tt);
}
while (temp1 != NULL) {
        sum = temp1->val + carry;
        temp1->val = sum % 10;
        carry = sum / 10;
        last = temp1;
        temp1 = temp1->next;
    }

if(carry!=0 && temp1==NULL && temp2==NULL)
{
    struct ListNode* new;
    new=malloc(sizeof(struct ListNode));
    new->val=carry;
    new->next=NULL;
    last->next=new;
}
return l1;
}
//______________________________________________________________________________________________________________________________________________________________________________________________
//Approach1: chatgpt corrected code. All test cases passed. Beat 99.9% in memory but only 14% in speed
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* temp1 = l1;
    struct ListNode* temp2 = l2;
    struct ListNode* last = NULL;
    int carry = 0;
    int sum;

    while (temp1 != NULL && temp2 != NULL) {
        sum = temp1->val + temp2->val + carry;
        temp1->val = sum % 10;
        carry = sum / 10;

        last = temp1;
        temp1 = temp1->next;
        temp2 = temp2->next;
    }

    if (temp2 != NULL) {
        if (last != NULL) {
            last->next = temp2;
            temp1 = last->next;
        } else {
            l1 = temp2;
            temp1 = l1;
        }
    }

    while (temp1 != NULL) {
        sum = temp1->val + carry;
        temp1->val = sum % 10;
        carry = sum / 10;
        last = temp1;
        temp1 = temp1->next;
    }

    if (carry != 0) {
        struct ListNode* new = malloc(sizeof(struct ListNode));
        new->val = carry;
        new->next = NULL;

        if (last != NULL) {
            last->next = new;
        } else {
            l1 = new;
        }
    }

    return l1;
}

//___________________________________________________________________________________________________________________________________________________________________
//Approach 2: Convert LInkedList to integer then add the two numbers then create a linked list and return.
//This approach is not very efficient as it requires to traverse both the lists multiple times.
