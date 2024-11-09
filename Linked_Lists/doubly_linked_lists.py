
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedList:
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
            #set the previous node to the current tail
            new_node.prev = self.tail
            # set the tail to the new node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        # sets temp to current head
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # sets temp to the next head
            self.head = self.head.next
            self.head.prev = None
            # removes the head from the list
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            # start from the end of the list, until the index is reached, decrementing by 1 each time
            for _ in range(self.length - 1, index, - 1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        # get the node before the index
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
    
    def remove_node(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        # get the node
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

my_doubly_list = DoublyLinkedList(7)
my_doubly_list.append(4)
my_doubly_list.append(5)
my_doubly_list.print_list()
# my_doubly_list.pop()
my_doubly_list.prepend(2)
my_doubly_list.pop_first()
my_doubly_list.print_list()
my_doubly_list.insert(1, 10)
my_doubly_list.remove_node(1)
my_doubly_list.print_list()