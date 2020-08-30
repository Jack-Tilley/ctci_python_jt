# 2.1
from linkedlist import Node
import unittest

def remove_dups(node):
    dic = {}
    head = node
    prev = node
    if head.nxt is None:
        return head
    curr = head.nxt
    dic[prev.data] = 1
    while curr.nxt is not None:
        dic[curr.data] = dic.get(curr.data, 0) + 1
        if dic[curr.data] > 1:
            curr = curr.nxt
            prev.nxt = curr
        else:
            prev = curr
            curr = curr.nxt
    if dic.get(curr.data, 0) >= 1:
        prev.nxt = None
    return head

class Test(unittest.TestCase):
  def test_remove_duplicates(self):
    head = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))
    remove_dups(head)
    print(head)
    self.assertEqual(head.data, 1)
    self.assertEqual(head.nxt.data, 3)
    self.assertEqual(head.nxt.nxt.data, 5)
    self.assertEqual(head.nxt.nxt.nxt, None)

if __name__ == "__main__":
  unittest.main()
