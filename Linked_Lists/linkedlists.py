# Big O Notation for linked lists:
# Append - O(1)
# Pop - O(n)
# Prepend - O(1)
# Pop First - O(1)
# Insert - O(n)
# Remove - O(n)
# Lookup - O(n)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # set the next value of the current tail to the new node
            self.tail.next = new_node
            # set the tail to the new node
            self.tail = new_node
        self.length += 1
        return True
    def pop(self):
        # empty list
        if self.length == 0:
            return None
        # set pointer to head
        temp = self.head
        #print(id(temp))
        # set pre to head
        pre = self.head
        # temp.next is not none
        while(temp.next):
            # set pre to temp.head, this will set 
            pre = temp
            #print(id(pre))
            # set temp to temp.next
            temp = temp.next
            #print(id(temp))
        # once temp.next is none, set self.tail to pre (temp.head)
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        # if removing creates a empty list
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    def pop_first(self):
        if self.length == 0:
            return None
        # sets temp to current head
        temp = self.head
        # sets temp to the next head
        self.head = self.head.next
        # removes the head from the list
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail == None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        # set temp at the beginning
        temp = self.head
        # underscore is used when not using a variable such as i
        for _ in range(index):
            # moves temp along linked list
            temp = temp.next
        return temp
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    def insert(self, index, value):
        new_node = Node(value)
        temp = self.get(index)
        pre = self.get(index)
        if temp:
            new_node.next = self.head
            self.head = new_node
            return True
        return False

# test statements
my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.print_list()
my_linked_list.set_value(1, 55)
my_linked_list.print_list()
my_linked_list.insert(1, 68)
my_linked_list.print_list()