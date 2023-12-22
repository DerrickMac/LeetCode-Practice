def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
    # create dummy node to hold head of new LL
    dummy = ListNode()
    
    # create tail pointer to hold last node of new LL
    tail = dummy

    # iterate through both LLs while both exist
    while list1 and list2:

        # compare values of both LLs
        # add smaller value to new LL
        # advance pointer of smaller value LL
        if list1.val < list2.val:
            tail.next = list1 
            list1 = list1.next 
        else:
            #
            tail.next = list2
            list2 = list2.next
        
        # advance tail pointer
        tail = tail.next
    
    # add remaining nodes of LL to new LL
    if list1:
        tail.next = list1

    elif list2:
        tail.next = list2

    return dummy.next