class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Use l1 as the result list - NO new nodes unless absolutely needed
        head = l1
        carry = 0
        
        # Phase 1: While both lists have nodes
        while l2:
            l1.val += l2.val + carry
            carry = l1.val // 10
            l1.val %= 10
            
            # If l2 has more nodes but l1 doesn't, borrow l2's nodes
            if l1.next is None and l2.next is not None:
                l1.next = l2.next
                l2.next = None
                l1 = l1.next
                break
            
            # If both end but carry remains, need one new node
            if l1.next is None and l2.next is None:
                if carry:
                    l1.next = ListNode(carry)
                return head
            
            l1 = l1.next
            l2 = l2.next
        
        # Phase 2: Process remaining digits with carry
        while carry:
            if l1 is None:
                l1 = ListNode(carry)
                break
            
            l1.val += carry
            carry = l1.val // 10
            l1.val %= 10
            
            if carry and l1.next is None:
                l1.next = ListNode(0)
            
            l1 = l1.next
        
        return head