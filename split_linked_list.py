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

    def add_at_end(self,data):
        temp=Node(data)
        current=self.head
        while current.next:
            current=current.next

        current.next=temp


    def get_size(self):
        size=0
        current=self.head
        while current is not None:
            current=current.next
            size+=1
        print("the size of linked list is {}".format(size))
        return size

    def split_linked_list(self,n,m):
        if self.get_size()!=(n+m):
            print("divide not possible")
        else:
            current=self.head
            while n > 1:
                current=current.next
                n-=1
            temp=current.next
            current.next=None
            return temp

    def print_linked_list(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next




def main():
    ll=LinkedList()
    ll.add_at_head(5)
    ll.add_at_end(6)
    ll.add_at_end(7)
    ll.add_at_end(8)
    ll.add_at_end(9)
    ll.add_at_end(10)
    ll.print_linked_list()

    n,m=input("enter size for splitting list\n").split(",")

    ll2=LinkedList()
    ll2.head=ll.split_linked_list(int(n),int(m))

    print("after splitting two list")

    print("first")
    ll.print_linked_list()
    print("second")
    ll2.print_linked_list()


if __name__ == '__main__':
    main()
