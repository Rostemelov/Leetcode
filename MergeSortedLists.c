/*
Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){

    struct ListNode* head;
    struct ListNode* last;
    if(l1==NULL && l2==NULL){return NULL;}
    else if(l1==NULL){return l2;}
    else if(l2==NULL){return l1;}
    if(l1->val < l2->val)
    {
        head=l1;
        last=head;
        l1=l1->next;
    }
    else
    {
        head=l2;
        last=head;
        l2=l2->next;
    }
    while(l1!=NULL && l2!=NULL)
    {
        if(l1->val < l2->val)
        {
            last->next=l1;
            last=last->next;
            l1=l1->next;
        }
        else
        {
            last->next=l2;
            last=last->next;
            l2=l2->next;
        }
    }
    while(l1!=NULL)
    {
        last->next=l1;
        last=last->next;
        l1=l1->next;
    }
    while(l2!=NULL)
    {
        last->next=l2;
        last=last->next;
        l2=l2->next;
    }
    last->next=NULL;
    return head;
}
