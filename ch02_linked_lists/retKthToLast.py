from linkedlist import Node
import unittest
def kth_to_last(node, k):
    ll = []
    ll.append(node)
    n = node
    length = 1
    while n.nxt:
        n = n.nxt
        ll.append(n)
        length += 1
    ll.append(n)
#     if k > length:
#         return - 1
    return ll[length - k]

class Test(unittest.TestCase):
  def test_kth_to_last(self):
    head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7, None)))))))
    # self.assertEqual(None, kth_to_last(head, 0));
    # self.assertEqual(7, kth_to_last(head, 1).data);
    # self.assertEqual(4, kth_to_last(head, 4).data);
    # self.assertEqual(2, kth_to_last(head, 6).data);
    # self.assertEqual(1, kth_to_last(head, 7).data);
    # self.assertEqual(None, kth_to_last(head, 8));

if __name__ == "__main__":
  unittest.main()
