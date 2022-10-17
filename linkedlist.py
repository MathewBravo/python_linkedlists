class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
            self.length += 1

    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
            self.length += 1

    def insert(self, value, index):
        node = Node(value)
        if index >= self.length:
            return
        elif index == self.length:
            return self.append(value)
        elif index == 0:
            return self.prepend(value)
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
        node.next = temp.next
        temp.next = node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_front(self):
        if self.length == 0:
            return None
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def get(self, index):
        if index >= self.length or index < 0:
            print("Out of range.")
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        elif index == self.length:
            return self.pop()
        elif index == 0:
            return self.pop_front()
        prev = self.get(index - 1)
        # O(1) assignment of temp
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        prev = None
        for _ in range(self.length):
            after = temp.next
            temp.next = prev
            prev = temp
            temp = after

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()
