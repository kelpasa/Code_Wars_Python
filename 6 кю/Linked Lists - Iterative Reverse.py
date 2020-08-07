'''https://www.codewars.com/kata/55e72695870aae78c4000026/train/python'''

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if not head:
            return None

    node = head
    node_new = None
    while node:
        if node_new:
            node_ = node_new
            node_new = Node(node.data)
            node_new.next = node_
        else:
            node_new = Node(node.data)
        node = node.next

    head.data = node_new.data
    head.next = node_new.next
