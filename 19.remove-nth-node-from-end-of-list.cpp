/*
 * @lc app=leetcode id=19 lang=cpp
 *
 * [19] Remove Nth Node From End of List
 *
 * https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
 *
 * algorithms
 * Medium (34.13%)
 * Total Accepted:    376.9K
 * Total Submissions: 1.1M
 * Testcase Example:  '[1,2,3,4,5]\n2'
 *
 * Given a linked list, remove the n-th node from the end of list and return
 * its head.
 * 
 * Example:
 * 
 * 
 * Given linked list: 1->2->3->4->5, and n = 2.
 * 
 * After removing the second node from the end, the linked list becomes
 * 1->2->3->5.
 * 
 * 
 * Note:
 * 
 * Given n will always be valid.
 * 
 * Follow up:
 * 
 * Could you do this in one pass?
 * 
 */

 // Definition for singly-linked list.
//  struct ListNode {
//         int val;
//         ListNode *next;
//         ListNode(int x) : val(x), next(NULL) {}
//   };
#include <stdlib.h> 

class Solution {
    //做题要举一反三，这题没相当完全因为没有通过找中间node题目发散思维
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* curr = head;
        ListNode* ahead = head;
        for(int i = 0; i < n; i++){
            ahead = ahead->next;
        }
        while(ahead->next) {
            curr = curr->next;
            ahead = ahead->next;
        }
        if(curr->next){
            curr->next = curr->next->next;
        } else {
            curr->next = nullptr;
        }
        

        return head;
    }
};
