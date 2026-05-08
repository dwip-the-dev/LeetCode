class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)       # Dummy head
        current = dummy           # Pointer to build result list
        carry = 0                 # Stores carry-over digit
        
        # Continue while there's something to process
        while l1 or l2 or carry:
            # Get current digits (0 if list has ended)
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            
            # Add everything together
            total = digit1 + digit2 + carry
            
            # The new digit is ones place, carry is tens place
            carry = total // 10
            digit = total % 10
            
            # Create and link the new node
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next