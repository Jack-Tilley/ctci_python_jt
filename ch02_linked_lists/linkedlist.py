class Node():
    def __init__(self, data, nxt):
        self.data = data
        self.nxt = nxt
        
    def append_to_tail(self, val):
        n = self
        while n.nxt is not None:
            n = n.nxt
        n.nxt = Node(val, None)
        
    def delete_node(self, val):
        head = self
        n = self
        if head.data == val:
            return head.nxt
        while n.nxt is not None:
            if n.nxt.data == val:
                n.nxt = n.nxt.nxt
                return head
            n = n.nxt
        return head

    def __str__(self):
        out = ""
        n = self
        while n.nxt is not None:
            out += str(n.data)
            out += ","
            n = n.nxt
        out += str(n.data)
        return out