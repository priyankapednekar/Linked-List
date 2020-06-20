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

    def add_at_index(self,index,data):
        n=index-1
        temp=Node(data)
        current=self.head
        if n!=0:
            for i in range(1,n):
                current=current.next
            # print("{} current index at {}".format(current.data,n))
            temp.next=current.next
            current.next=temp
        else:
            self.add_at_head(data)

    def remove_at_index(self,index):
        current=self.head
        n=index-1
        if n!=0:
            for i in range(1,n):
                current=current.next

            current.next=current.next.next
        else:
            self.head=current.next

    def get_size(self):
        size=0
        current=self.head
        while current is not None:
            current=current.next
            size+=1
        print("the size of linked list is {}".format(size))

    def search_item(self,data):
        current=self.head
        while current is not None:
            if current.data==data:
                print("Found {} !!".format(data))
                return
            else:
                current=current.next
        print("Item  {} Not Present!!".format(data))

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
    ll.add_at_end(8)
    ll.add_at_index(2,9)
    ll.print_linked_list()

    ll.remove_at_index(5)
    print("after removal node at index mentioned above")
    ll.print_linked_list()

    ll.get_size()

    ll.search_item(int(input("enter item for search\n")))


if __name__ == '__main__':
    main()
