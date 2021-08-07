# https://www.algoexpert.io/questions/Reverse%20Linked%20List
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    current = head
    previous = None

    while current is not None:
        hold = current.next
        current.next = previous
        previous = current
        current = hold

    return previous