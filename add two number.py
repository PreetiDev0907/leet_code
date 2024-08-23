class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    # Create a dummy node to act as the start of the result list
    dummy = ListNode(0)
    # Pointer for the current node in the result list
    current = dummy
    carry = 0
    
    # Traverse both lists
    while l1 or l2 or carry:
        # Get the values from the nodes (0 if the node is None)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Compute the sum of values and carry
        total = val1 + val2 + carry
        
        # Update the carry for the next iteration
        carry = total // 10
        
        # Create a new node with the digit value
        current.next = ListNode(total % 10)
        
        # Move to the next node in the result list
        current = current.next
        
        # Move to the next nodes in the input lists
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    # Return the result list, starting from the next node of the dummy
    return dummy.next

# Helper function to convert a list to a linked list
def list_to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for item in lst:
        current.next = ListNode(item)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linked_list_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

# Example usage:
l1 = list_to_linked_list([2, 4, 3])  # Represents the number 342
l2 = list_to_linked_list([5, 6, 4])  # Represents the number 465
result = add_two_numbers(l1, l2)
print(linked_list_to_list(result))  # Output: [7, 0, 8] which represents 807
