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

# Function to find the nth node from end of Linked List


def find_nth(lst, n):
    # Use two pointers. Advance once of the two by n nodes and then move the two together until forward one reaches the end.
    # At that time behind one is pointing at answer
    
    if lst is None:
        return -1

    head = lst.get_head()

    behind = head
    forward = head
    for i in range(n):
        if forward.next_element:
            forward = forward.next_element
        else:
            return -1
    
    while forward.next_element:
        forward = forward.next_element
        behind = behind.next_element
        
    behind = behind.next_element
    
    return behind.data


lst1 = LinkedList()
lst1.insert_at_head(21)
lst1.insert_at_head(14)
lst1.insert_at_head(7)
lst1.insert_at_head(8)
lst1.insert_at_head(22)
lst1.insert_at_head(15)

result = find_nth(lst1 ,4)
print(result)
result = find_nth(lst1 ,5)
print(result)
result = find_nth(lst1 ,8)
print(result)

## output ##
# 8
# 22
# -1
