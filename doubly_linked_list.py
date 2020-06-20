class Node():

    def __init__(self, data):
        self.data = data
        self.prev=None
        self.next=None


class doublyLinkedlist():
    """docstring for Linkedlist."""

    def __init__(self):
        self.head = None
        self.tail= None
        self.count=0

    def add_at_head(self,data):
        temp=Node(data)
        current=self.head
        if current:
            temp.next=current
            temp.prev=None
            current.prev=temp
            self.head=temp
            self.count+=1
        else:
            self.head=temp
            self.tail=temp
            self.count+=1

    def add_at_tail(self,data):
        temp=Node(data)
        current=self.tail
        if current:
            temp.next=None
            temp.prev=current
            current.next=temp
            self.tail=temp
            self.count+=1
        else:
            self.head=temp
            self.tail=temp
            self.count+=1

    def add_at_index(self,index,data):
        temp=Node(data)
        current=self.head
        if index > 1 and index < self.count :
            for i in range(1,index):
                current=current.next

            temp.next=current
            temp.prev=current.prev
            current.prev.next=temp
            self.count+=1
        elif index <= 1:
            self.add_at_head(data)
        elif index == self.count:
            self.add_at_tail(data)

    def print_linked_list(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next


def main():
    dl=doublyLinkedlist()
    dl.add_at_head(5)
    dl.add_at_head(6)
    dl.add_at_tail(7)
    dl.add_at_index(3,8)
    dl.print_linked_list()
    print("the doublyLinkedlist count is : {}".format(dl.count))

if __name__ == '__main__':
    main()
