class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = curr = ListNode(0)
        carry = 0
        
        while l1 and l2:
            carry, digit = divmod(l1.val + l2.val + carry, 10)
            curr.next = ListNode(digit)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        # Only one list remains (or none)
        remaining = l1 or l2
        while remaining:
            carry, digit = divmod(remaining.val + carry, 10)
            curr.next = ListNode(digit)
            curr = curr.next
            remaining = remaining.next
        
        # Final carry
        if carry:
            curr.next = ListNode(1)
        
        return dummy.next