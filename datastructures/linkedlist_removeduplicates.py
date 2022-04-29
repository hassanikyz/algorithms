"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

"""
   
   def deleteDuplicates( head: Optional[ListNode]) -> Optional[ListNode]:


        # key idea is you create a new dummy node so you don't lose track of the original 
        # head node and move the move the head forward until duplicates are found.
        # once duplicates are found move head all the way to last dup 
        # then behind pointer will be used to point the 'next' of behind to the next of current head
        # now you move the head forward as well.
        # the third sentinel pointer is always our new head to be returned. 
        
        behind = ListNode()
        sentinel = behind
        behind.next = head
        
        while head:
            
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                behind.next = head.next
            else:
                behind = behind.next
                
            head = head.next
        return sentinel.next
     
    
   
