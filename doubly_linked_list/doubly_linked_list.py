"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.head == None:
            self.head = ListNode(value)
            self.tail = self.head
            self.length += 1
        elif self.head == self.tail:
            self.head = ListNode(value)
            self.head.next = self.tail
            self.tail.prev = self.head
            self.length += 1
        elif self.length >= 2:
            self.head.prev = ListNode(value, None, self.head)
            self.head = self.head.prev
            self.length += 1

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        val = self.head.value
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.length >= 2:
            self.head = self.head.next
            self.length -= 1

        return val
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.tail == None:
            self.tail = ListNode(value)
            self.head = self.tail
            self.length += 1
        elif self.head == self.tail:
            self.tail = ListNode(value)
            self.tail.prev = self.head
            self.head.next = self.tail
            self.length += 1
        elif self.length >= 2:
            self.tail.next = ListNode(value, self.tail, None)
            self.tail = self.tail.next
            self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        val = self.tail.value
        if self.length == 1:
            self.tail = None
            self.head = None
            self.length -= 1
        elif self.length >= 2:
            self.tail = self.tail.prev
            self.length -= 1 
        return val
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node.prev is not None:
            self.delete(node)
            self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node.next is not None:
            self.delete(node)
            self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None or node is None: 
            return
        
        if self.head == node: 
            self.head = node.next

        if self.tail == node:
            self.tail = node.prev

        if node.next is not None: 
            node.next.prev = node.prev

        if node.prev is not None: 
            node.prev.next = node.next 

        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        maxVal = self.head.value
        nextNode = self.head.next
        while nextNode is not None:
            if maxVal <= nextNode.value:
                maxVal = nextNode.value
            nextNode = nextNode.next

        return maxVal