
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""

def merge_sorted_linked_list(list1, list2):
  
      list1ptr = list1
      list2ptr = list2

      fwdptr = list1
      head = None

      while list1ptr and list2ptr:

          while (list1ptr.next and list1ptr.next.val <= list2ptr.val):
              list1ptr = list1ptr.next

          while (list2ptr.next and list2ptr.next.val < list1ptr.val):
              list2ptr = list2ptr.next

          if list1ptr.val <= list2ptr.val:
              fwdptr = list1ptr.next
              list1ptr.next = list2ptr
              list1ptr = fwdptr

              if head is None:
                  head = list1

          else:
              fwdptr = list2ptr.next
              list2ptr.next = list1ptr
              list2ptr = fwdptr

              if head is None:
                  head = list2


      return head
