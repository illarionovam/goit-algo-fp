class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None

  def print_list(self):
    current = self.head
    while current:
      print(current.data, end=" ")
      current = current.next
    print()

  def reverse(self):
    """написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;"""
    prev = None
    current = self.head

    while current:
        # запамʼятали, який вузол буде ннаступним, бо зараз затремо посилання
        next_node = current.next
        # реверснули посилання на поточному вузлі
        current.next = prev
        prev = current
        current = next_node

    self.head = prev

def merge_lists(l1, l2):
   """написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список."""
   ans = LinkedList()
   ans.head = merge(l1.head, l2.head)
   return ans

def merge(l1, l2):
    ans = Node(11) # вузол, щоб розпочати, ми його викинемо у кінці
    current = ans

    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    else:
        current.next = l2

    return ans.next

def get_mid(head):
    slow = head
    fast = head

    while fast.next and fast.next.next:
        # метод подвійних стрибків
        slow = slow.next
        fast = fast.next.next

    return slow

def merge_sort_list(llist):
   """розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;"""
   ans = LinkedList()
   ans.head = merge_sort(llist.head)
   return ans

def merge_sort(head):
   if head is None or head.next is None:
        # якщо в нас <= 1 елемента
        return head
   
   mid = get_mid(head)
   mid_next = mid.next
   mid.next = None

   left = merge_sort(head)
   right = merge_sort(mid_next)
   ans = merge(left, right)

   return ans
      
llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

llist.print_list()
llist.reverse()
llist.print_list()

llist = merge_sort_list(llist)
llist.print_list()

llist1 = LinkedList()
llist1.insert_at_end(1)
llist1.insert_at_end(3)
llist1.insert_at_end(5)

llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(4)
llist2.insert_at_end(6)

llist3 = merge_lists(llist1, llist2)
llist3.print_list()