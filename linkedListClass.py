
class listNode:
    def __init__(self, data):
        self.data = data
        self.next = None

head_node = listNode(1)
second_node = listNode(2)

head_node.next = second_node
second_node.next = head_node

print(head_node.data)
print(second_node.data)