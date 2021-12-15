# https://leetcode.com/problems/linked-list-cycle
# https://www.youtube.com/watch?v=gBTe7lFR3vc
# O(n) time with the length being the length of the cycle
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Its possible the list could be empty, so there would be no cycle
        if head == None:
            return False
        # This solution uses 2 pointers (tortise and hare algorithim)
        slow = head;
        fast = head;
        # While both are not null
        while fast and fast.next:
            # Both start out at the same position, but the fast pointer is incremented twice each time
            slow = slow.next
            fast = fast.next.next
            # At some point if there is a cycle, the fast pointer will catch back up the slow pointer
            if slow == fast:
                return True
        return False
