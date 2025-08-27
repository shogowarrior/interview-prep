# Find cycle in Linked List
from linkedlist import LinkedList


def create_linked_list(cycle = False):
    ll = LinkedList()
    input_list = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in input_list:
        ll.append(i)
    # Add cycle
    ll.create_cycle(4) if cycle is True else None
    return ll


def detect_cycle(ll : LinkedList):
    ptr_1 = ll.head
    ptr_2 = ll.head

    while ptr_2 and ptr_2.next:
        ptr_1 = ptr_1.next
        ptr_2 = ptr_2.next.next
        if ptr_1 == ptr_2:
            print("cycle detected")
            return
        
if __name__ == "__main__":
    # Create linked list
    ll_1 = create_linked_list(False)
    ll_1.display()
    detect_cycle(ll_1)


    ll_2 = create_linked_list(True)
    detect_cycle(ll_2)



    








    
