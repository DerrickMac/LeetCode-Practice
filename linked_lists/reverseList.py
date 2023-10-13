def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # use a two pointer method: previous pointer and current pointer
    prev, curr = None, head

    # iterate through LL while current node exists
    while curr:

        # create third pointer to hold the next node
        next = curr.next
        
        # change curr's pointer to previous node
        curr.next = prev

        # advance prev pointer to current node
        prev = curr    
        
        # advance curr pointer to next node
        curr = next
    
    # new head is now prev pointer
    return prev