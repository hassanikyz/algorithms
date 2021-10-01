

from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Remove duplicates => list.remove_duplicates()
# Node class  {int data ; Node next_element;}

# Returns a list containing the union of list1 and list2


def union(list1, list2):
    # Write your code here
    head1 = list1.get_head()
    head2 = list2.get_head()
    last1 = head1
    while last1.next_element:
        last1 = last1.next_element
    last1.next_element = head2
    list1.remove_duplicates()
    return list1

# Returns a list containing the intersection of list1 and list2


def intersection(list1, list2):
    # Write your code here

    list1.remove_duplicates()
    list2.remove_duplicates()
    
    list1len = list1.length()
    list2len = list2.length()
    
    mydict = {}
    head1 = list1.get_head()
    while head1.next_element:
        mydict[head1.data] = 1
        head1  = head1.next_element
    mydict[head1.data] = 1

    head2 = list2.get_head()
    listofkeys = mydict.keys()
    while head2:
        if head2.data not in mydict.keys():
            list2.delete(head2.data)

        head2 = head2.next_element
            
    return list2

list1 = LinkedList()
list1.insert_at_head(14)
list1.insert_at_head(22)
list1.insert_at_head(15)

list2 = LinkedList()
list2.insert_at_head(21)
list2.insert_at_head(14)
list2.insert_at_head(15)
list3 = intersection(list1, list2)
list3.print_list()

### expected output ###
## 15 -> 14 -> None
