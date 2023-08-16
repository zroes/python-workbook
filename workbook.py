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

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'
# print(node)
# print(serialize(node))
# print(deserialize(serialize(node)))


# NOTE Day 4
def low_pos_int(arr):
  v = 1
  for i in sorted(arr):
    if i == v:
      v += 1
  return v


# NOTE Day 5
def cons(a, b):
  def pair(f):
    return f(a, b)
  return pair

def car(pair):
  return pair(lambda a, b : a)

def cdr(pair):
  return pair(lambda a, b : b)

# print(cons(4, 5))
# print(car(cons(4, 5)))
# print(cdr(cons(4, 5)))

# NOTE Day 7
# Needed lots of assistance with this one
# Overall it's a relatively basic dynamic programming problem, but this was my first intro to dp. 
def decode(message):
  total = 1
  for i in range(len(message)):
    print(i, total)
    if int(message[i]) == 1:
      try:
        message[i + 1]
        total += 1
      except IndexError as e:
        pass
  return total

def decode_d(message):
    message_len = len(message)

    number_of_solutions = [0] * (message_len + 1)
    number_of_solutions[0] = 1
    number_of_solutions[1] = 1

    for i in range(2, message_len+1):
        last_digit = int(message[i-1])
        two_last_digits = int(message[(i-2):i])
        # If the last digit is greater than zero, 
        # then the number of solutions stays the same
        if (last_digit > 0):
            number_of_solutions[i] = number_of_solutions[i - 1]

        # If the two last digits are in between 9 and 27, 
        # this results in an additional batch of solutions.
        # Thus, a number of the solutions from two characters before is added.
        if ((two_last_digits > 9) & (two_last_digits < 27)):  
            number_of_solutions[i] += number_of_solutions[i - 2]  

    return number_of_solutions[-1]

def decode_dp(s):
  l = len(s)
  dp = [0] * l
  dp.append(1)
  print(dp)
  # basically, dp represents each 'layer' of recursion, if we were to solve this with recursion.
  # For each layer, we add the total solutions from the previous layer
  # if the value at isn't at the end, and is equal to 1 or 2, then we add the solutions from the previous previous layer as well 
  for i in range(l - 1, -1, -1):
    if s[i] == '0':
      continue
    dp[i] += dp[i+1]
    if i + 1 < l and (s[i] <= '1' or (s[i] == '2' and s[i+1] <= '6')):
      dp[i] += dp[i+2]
  print(dp)
  return dp[0]

# print(decode_d('1114512'), decode('1114512'))

# NOTE Day 11
def autocomp(s: str, words: set):
    return [word for word in words if word.startswith(s)]

# print(autocomp('dea', ["deer", "dear", "deal", "deep", "dead", "dean"]))

def run_len(s: str):
  output = ""
  l = len(s)
  i = 0
  while i < l - 1:
    count = 1
    while  i < l - 1 and s[i + 1] == s[i]:
      # print(s[i], i)
      count += 1
      i += 1
    output += f"{count}{s[i]}"
    i+=1
    # print(n)
    # print(output)
  return output

print(run_len("AAAABBBCCDAA"))

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
