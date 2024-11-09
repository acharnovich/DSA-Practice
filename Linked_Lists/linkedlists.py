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
    # method inserts at the beginning of the list
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
    # method to pop off the head of the lest
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
    # provided a index, gets the node 
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
    # sets the value of a node providing a index
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    # inserts a node based on provided index
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove_node(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        # temp = self.get(index) // this is no good because it is O(n)
        temp = prev.next # this method works better because it is O(1)
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            # sets temp backwards one node
            temp.next = before
            # before needs to be set prior to temp, so that it doesn't break the link between temp and after
            before = temp
            temp = after
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(fast.head.value)
        return slow   
    def has_loop(self):
        slow  = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
    def remove_duplicates(self):
        unique = set()
        current = self.head
        prev = None
        while current:
            if current.value in unique:
                prev.next = current.next
                self.length -= 1 
            else:
                unique.add(current.value)
                prev = current
            current = current.next
    def binary_to_decimal(self):
        current = self.head
        decimalNum = 0
        
        while current:
                decimalNum = decimalNum * 2 + current.value
                print(decimalNum)
                current = current.next
        return decimalNum 
    
def find_kth_from_end(LinkedList, k):
    slow = my_linked_list.head
    fast = my_linked_list.head
    if LinkedList.head == None:
        return None
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow

            

# test statements
my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.print_list()
my_linked_list.remove_duplicates()
my_linked_list.print_list()
