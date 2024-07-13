class Node:
    def __init__(self, data):
        self.data = data  # Dato que contiene el nodo
        self.next = None  # Referencia al siguiente nodo

class LinkedList:
    def __init__(self):
        self.head = None  # La cabeza de la lista enlazada

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Crear una lista enlazada y añadir algunos nodos
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# Imprimir la lista enlazada
linked_list.print_list()
