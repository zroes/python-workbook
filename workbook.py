import time
# import assert
# steps is an int that describes how many steps are in a staircase
# solution will return the number of different ways someone could climb the stairs, if they could climb either 1 or 2 steps at a time
# from experimenting, we see:
# solution(4) => 5 which is solution(3) + solution(2)

# this holds true for solution(6) => 13 = solution(4) => 5 + solution(5) => 8

# recursion 
def steps(n):
  if n <= 1:
    return 1
  return steps(n - 1) + steps(n - 2)


# iterative
def steps_b(n):
  a, b = 1, 2
  for _ in range(n - 1):
    a, b = b, a + b
  return a



# NOTE Day One ----------------------------
# basic
def p_one(list, k):
  for i in list:
    for j in range(len(list)):
      if i + list[j] == k and i != list[j]:
        return True
  return False

# set
# the advantage of using a set is that it's very fast to search a set for a value.
# for larger lists, it's worth the tradeoff of time to create the set from the list
def p_one_set(list, k):
  hashset = set(list)
  for i in list:
    if k - i in hashset:
      return True
  return False 



# NOTE Day Two ---------------------------
# with division
def p_two_div(list):
  arr = []
  prod = 1
  for i in list:
    prod *= i
  for i in list:
    arr.append(prod / i)
  return arr

# no division
def p_two(list):
  arr = []
  prod = 1
  for i in list:
    prod = 1
    for j in list:
      if j != i:
        prod *= j
    arr.append(prod)
  return arr


# O(n) solution from stack
def p_two_good(list):
  n = len(list)
  products_below = []
  prod = 1
  for i in range(n):
    products_below.append(prod)
    prod *= list[i]
  # print(products_below)

  products_above = []
  prod = 1
  for i in reversed(range(n)):
    products_above.append(prod)
    prod *= list[i]
  products_above.reverse()
  # print(products_above)

  products = []
  for i in range(n):
    products.append(products_above[i] * products_below[i])

  return products

# print(p_one_set([10,15,3,7], 12))
# print(p_two([1, 2, 3, 4, 5]))
# print(p_two_good([1, 2, 3, 4, 5]))

# NOTE Day Three --------------------------
# I had no idea how to even start this one...
class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def serialize(node):
  val = node.val
  if node.left:
    left = serialize(node.left)
  else:
    left = None
  if node.right:
    right = serialize(node.right)
  else:
    right = None

  serialized = [val, left, right]
  return serialized

def deserialize(serialzed_node):
  val = serialzed_node[0]
  if serialzed_node[1]:
    left = deserialize(serialzed_node[1])
  else:
    left = None

  if serialzed_node[2]:
    right = deserialize(serialzed_node[2])
  else:
    right = None

  return Node(val, left, right)

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
print(node)
print(serialize(node))
print(deserialize(serialize(node)))

# NOTE timer stuff
# t0 = time.time()
# for _ in range(10000):
#   p_two([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30])
# t1 = time.time()
# print(t1 - t0)

# t0 = time.time()
# for _ in range(10000):
#   p_two_div([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30])
# t1 = time.time()
# print(t1 - t0)


# t0 = time.time()
# for _ in range(10000):
#   p_two_good([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30])
# t1 = time.time()
# print(t1 - t0)
