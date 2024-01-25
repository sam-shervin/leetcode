class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* l3 = new ListNode;
        ListNode* LL = l3;
        int carry = 0;
        int sum;
        while(l1!=nullptr && l2!=nullptr){
            l3->next = new ListNode;l3 = l3->next;
            sum = l1->val+l2->val+carry;
            l3->val = sum%10;
            carry = sum/10;
            l1 = l1->next; 
            l2 = l2->next;
        }
        while(l2!=nullptr && l1==nullptr){
            l3->next = new ListNode;l3 = l3->next;
            sum = l2->val+carry;
            l3->val = sum%10;
            carry = sum/10; 
            l2 = l2->next;
        }
        while(l1!=nullptr && l2==nullptr){
            l3->next = new ListNode;l3 = l3->next;
            sum = l1->val+carry;
            l3->val = sum%10;
            carry = sum/10; 
            l1 = l1->next; 
        }
        if(carry == 1){
            l3->next = new ListNode;
            l3->next->val = 1;
        }
        return LL->next;
    }
};