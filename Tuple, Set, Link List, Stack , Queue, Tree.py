#TUPLE EXAMPLE


my_tuple = (10, 20, 30)
print("Tuple:", my_tuple)
print("First element:", my_tuple[0])


#SET EXAMPLE


my_set = {1, 2, 3, 2, 1}   # duplicates removed
my_set.add(4)
print("\nSet:", my_set)
print("Contains 2:", 2 in my_set)

 
#LINKED LIST EXAMPLE

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

print("\nLinked List:")
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()


#STACK EXAMPLE


stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print("\nStack (LIFO):", stack)
print("Popped:", stack.pop())
print("Stack after pop:", stack)


#QUEUE EXAMPLE


from collections import deque

queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
print("\nQueue (FIFO):", queue)
print("Dequeued:", queue.popleft())
print("Queue after dequeue:", queue)


#TREE EXAMPLE


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("\nTree Preorder Traversal:")
preorder(root)
print()
