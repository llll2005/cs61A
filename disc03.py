"""
Q1: Recursive Multiplication
"""
def multiply(m, n):
    """Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n != 0 :
        return m + multiply(m, n-1)
    else:
        return 0
"""
Q2: Swipe
"""
def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        "*** YOUR CODE HERE ***"
        print(n % 10)
        swipe(n//10)
        print(n%10)
"""
Q3: Skip Factorial
"""
def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 0:
        return 1
    else:
        return n* skip_factorial(n-2)
"""
Q4: Recursive Hailstone
Recall the hailstone function from Homework 1. First, pick a positive integer n as the start. If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. Repeat this process until n is 1. Complete this recursive version of hailstone that prints out the values of the sequence and returns the number of steps.
"""
def hailstone(n):
    """Print out the hailstone sequence starting at n,
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n == 1:
        return 1
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)
def even(n):
    return 1+hailstone(n//2)

def odd(n):
    "*** YOUR CODE HERE ***"
    return 1+hailstone(3*n+1)
"""
Q5: Count Stair Ways
Imagine that you want to go up a flight of stairs that has n steps, where n is a positive integer. You can take either one or two steps each time you move. In how many ways can you go up the entire flight of stairs?

You'll write a function count_stair_ways to answer this question. Before you write any code, consider:

How many ways are there to go up a flight of stairs with n = 1 step? What about n = 2 steps? Try writing or drawing out some other examples and see if you notice any patterns.
What is the base case for this question? What is the smallest input?
Now, fill in the code for count_stair_ways:
"""
def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either one step or two steps at a time.
    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)

"""
Q6: Subsequences
"""
def insert_into_all(item, nested_list):
    """Return a new list consisting of all the lists in nested_list,
    but with item added to the front of each. You can assume that
    nested_list is a list of lists.

    >>> nl = [[], [1, 2], [3]]
    >>> insert_into_all(0, nl)
    [[0], [0, 1, 2], [0, 3]]
    """
    "*** YOUR CODE HERE ***"
    return [[item] + lst for lst in nested_list]


def subseqs(s):
    """Return a nested list (a list of lists) of all subsequences of S.
    The subsequences can appear in any order. You can assume S is a list.

    >>> seqs = subseqs([1, 2, 3])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> subseqs([])
    [[]]
    """
    if not s:
        return [[]]
    else:
        rest_subseqs = subseqs(s[1:])
        return insert_into_all(s[0], rest_subseqs) + rest_subseqs
