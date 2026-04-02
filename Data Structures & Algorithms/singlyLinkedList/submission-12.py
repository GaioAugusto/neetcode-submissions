class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        counter = 0
        temp = self.head
        if self.head is None:
            return -1

        while temp != None:
            if counter == index:
                return temp.value
            temp = temp.next
            counter += 1
        
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        if index == 0:
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.next
            return True

        counter = 0
        temp = self.head
        while temp.next != None:
            if counter == index - 1:
                if temp.next == self.tail:
                    self.tail = temp
                temp.next = temp.next.next
                return True
            temp = temp.next
            counter += 1
        
        return False
        
    def getValues(self) -> List[int]:
        nodes = []
        temp = self.head
        while temp != None:
            nodes.append(temp.value)
            temp = temp.next
        return nodes