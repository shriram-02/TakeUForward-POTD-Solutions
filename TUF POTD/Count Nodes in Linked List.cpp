class Solution {
public:
    int countNodes(ListNode* head) {
        int count = 0;
        while (head != NULL) {
            count++;
            head = head->next;
        }
        return count;
    }
};