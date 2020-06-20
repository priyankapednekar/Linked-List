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


    def print_linked_list(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next


    def detect_loop_with_set(self):
        set1=set()
        current=self.head
        while current is not None:
            if current in set1:
                return True
            else:
                set1.add(current)
            current=current.next

    def detect_loop_with_pointer(self):
        fast=self.head
        slow=self.head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True

    def loop_len_with_pointer(self):
        fast=self.head
        slow=self.head
        count=1
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                slow=slow.next
                while  slow != fast:
                        slow=slow.next
                        count+=1
                return count

def main():
    ll=LinkedList()
    ll.add_at_head(5)
    ll.add_at_head(6)
    ll.add_at_head(7)
    ll.add_at_head(8)
    ll.add_at_head(10)

    ll.head.next.next.next = ll.head

    # ll.print_linked_list()
    '''detecting loop by using set'''
    print(ll.detect_loop_with_set())

    '''Floyd’s Cycle-Finding Algorithm'''
    print(ll.detect_loop_with_set())

    print("lenght of loop\n")
    print(ll.loop_len_with_pointer())

if __name__ == '__main__':
    main()
