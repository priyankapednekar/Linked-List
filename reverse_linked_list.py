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

    '''iteration'''
    def reverse_link_iter(self):
        prev=None
        current=self.head
        while current is not None:
            next=current.next
            current.next=prev
            prev=current
            current=next

        self.head = prev

    '''recursion'''
    def reverseUtil(self, curr, prev):

        # If last node mark it head
        if curr.next is None :
            self.head = curr

            # Update next to prev node
            curr.next = prev
            return

        # Save curr.next node for recursive call
        next = curr.next

        # And update next
        curr.next = prev

        self.reverseUtil(next, curr)

    def reverse(self):
        if self.head is None:
            return

        self.reverseUtil(self.head, None)



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

    ll.reverse_link_iter()

    print("after reverse")
    ll.print_linked_list()

    ll.reverse()

    print("after reverse")
    ll.print_linked_list()



if __name__ == '__main__':
    main()
