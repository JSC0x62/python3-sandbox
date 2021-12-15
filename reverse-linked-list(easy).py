# https://leetcode.com/problems/reverse-linked-list
# https://www.youtube.com/watch?v=G0_I-ZF0S38
# Iterative solution, O(n) time and O(1) memory
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 2 pointers to keep track of switching nodes. Previous node starts out as Null
        current = head
        previous = None
        
        # While the current node != null
        while current:
            # A tmp pointer to keep track of the next node before current.next is operated on
            nextNode = current.next
            # The next node = the previous one, and the previous is assigned the current node for the next iteration
            current.next = previous
            previous = current
            # Then the current is assigned to its original next, to be able to keep passing through the nodes
            current = nextNode
        # The previous is returned as now its the new head starting from where the tail used to be
        return previous
