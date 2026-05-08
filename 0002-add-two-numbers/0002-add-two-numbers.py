class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        prev = None
        carry = 0
        
        # Add l2 into l1
        while l1 and l2:
            total = l1.val + l2.val + carry
            l1.val = total % 10
            carry = total // 10
            prev = l1
            l1 = l1.next
            l2 = l2.next
        
        # Attach remaining l2 to l1 if l1 ended first
        if l2:
            prev.next = l2
            l1 = l2
        
        # Propagate carry through remaining nodes
        while carry and l1:
            total = l1.val + carry
            l1.val = total % 10
            carry = total // 10
            prev = l1
            l1 = l1.next
        
        # Only allocate if absolutely necessary
        if carry:
            prev.next = ListNode(carry)  # Only new node ever created
        
        return head