def reverseList(head):
	# Set a current pointer to head, and a previous pointer to Null
	prev, curr = None, head
	
	# iterate through entire LL and stop when curr is Null
	while curr:
	
		# save the reference of current node's next node
		nxt = curr.next
		
		# change the reference of current node to previous node
		curr.next = prev
		
		# move the previous node forward
		prev = curr
		
		# move the current node forward to the reference we saved in nxt
		curr = nxt
	
	# prev will become the new head of the reversed list, which is returned
	return prev
	 