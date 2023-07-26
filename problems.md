<!-- SECTION 1 -->
1. 
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

<!-- SECTION 2 -->
2. 
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?


<!-- SECTION 3 -->
3.
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

```py
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

The following test should pass:
```py
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```
solution: https://numbergeneral.github.io/dailycodingproblem03/
NOTES: This one was impossible for me and I had to search for a solution. If I can't figure out binary trees / linked lists next time, I'm going to need to look into a data structures course.



<!-- SECTION 4 -->
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.


<!-- SECTION 5 -->
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:
```py
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```
Implement car and cdr.

<!-- SECTION 7  (skipped 6) -->
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

NOTES: This was an intro to dynamic programming, yet another thing I need to learn more about
Resources: https://leetcode.com/problems/decode-ways/solutions/2795116/python-solution-explained-intuition-and-algorithm/
https://numbergeneral.github.io/dailycodingproblem07/




