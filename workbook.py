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



# Day One ----------------------------
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

print(p_one_set([10,15,3,7], 12))
  
    
  