class Node:
    """
    An object for storing a single node of a linked list.
    Model two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"

class LinkedList:
    """
    Singly linked link.
    """

    def __init__(self):
        self.head = None
    
    def is_empty(self):
        """
        Check if the LinkedList is empty
        Returns bool

        """
        return self.head == None
    
    def size(self):
        """
        Returns the numbers of nodes in the list
        Takes O(n) time
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        """
        Adds new Node containing data at head of the list.
        Takes O(1) time
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
    def search(self, key):
        """
        Search for the first node containing data that matches
        the key.
        Returns the node or 'None' if not found
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position.
        Insertion takes 0(1) but finding the node at the 
        insertion point takes 0(n) time.

        Takes overall 0(n) time
        
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = self.head.next_node
                position -= 1
            
            prev = current
            next_node = current.next_node

            prev_node = new
            new.next_node = next_node
        return None

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Returns the node or None if key doesn't exist
        Takes 0(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current


    def __repr__(self):
        """
        Returns a string representation of the list
        Takes O(n) time
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")

            current = current.next_node
        return '-> '.join(nodes)

    
    def node_at_index(self, index):
        if index == 0:
            return self.head
        
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1
            return current


l = LinkedList()
l.add(1)
l.add(4)
l.add(3)
l.add(2)
l.add(2)

l.insert(10, 5)
n = l.search(2)
print(l.is_empty())
print(n)


print(l)