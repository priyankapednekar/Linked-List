class Node():

    def __init__(self, data):
        self.data=data
        self.next = None

class LinkedList():

    def __init__(self):
        self.head = None

    def add_at_head(self,data):
        temp=Node(data)
        current=self.head
        if current:
            temp.next=current
            self.head=temp
        else:
            self.head=temp

    # Function to check the length of linklist
    def LinkedListLength(self):
        while (self.head != None and self.head.next != None):
            self.head = self.head.next.next

        if(self.head == None):
            return 0
        return 1

    def print_linked_list(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next

def main():

    ll=LinkedList()
    ll.add_at_head(5)
    ll.add_at_head(6)
    ll.add_at_head(7)
    ll.add_at_head(8)
    ll.add_at_head(10)

    ll.print_linked_list()

    check = ll.LinkedListLength()

    if(check == 0) :
        print("Even")
    else:
        print("odd")

if __name__ == '__main__':
    main()
