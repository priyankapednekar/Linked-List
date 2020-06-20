class Node():

    def __init__(self, data):
        self.data=data
        self.next = None

class LinkedList():

    def __init__(self):
        self.head = None

    def insert_node(self,data):
        temp=Node(data)
        current=self.head
        if current:
            while current.next is not None:
                current=current.next
            current.next=temp
        else:
            self.head=temp


    def print_linked_list(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next



'''recursive'''
# Function to merge two sorted linked list.
def mergeLists(head1, head2):

    # create a temp node NULL
    temp = None

    # List1 is empty then return List2
    if head1 is None:
        return head2

    # if List2 is empty then return List1
    if head2 is None:
        return head1

    # If List1's data is smaller or
    # equal to List2's data
    if head1.data <= head2.data:

        # assign temp to List1's data
        temp = head1

        # Again check List1's data is smaller or equal List2's
        # data and call mergeLists function.
        temp.next = mergeLists(head1.next, head2)

    else:
        # If List2's data is greater than or equal List1's
        # data assign temp to head2
        temp = head2

        # Again check List2's data is greater or equal List's
        # data and call mergeLists function.
        temp.next = mergeLists(head1, head2.next)

    # return the temp list.
    return temp





def main():

    ll1=LinkedList()
    ll1.insert_node(1)
    ll1.insert_node(2)
    ll1.insert_node(5)
    ll1.insert_node(7)
    ll1.insert_node(9)

    print("First list")

    ll1.print_linked_list()

    print("Second list")

    ll2=LinkedList()
    ll2.insert_node(3)
    ll2.insert_node(4)
    ll2.insert_node(6)
    ll2.insert_node(8)

    ll2.print_linked_list()

    ll3=LinkedList()

    ll3.head=mergeLists(ll1.head,ll2.head)

    print("\nMerged list")
    ll3.print_linked_list()



if __name__ == '__main__':
    main()
