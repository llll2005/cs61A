def race(x, y):
    """tortoise x feet/minute,
    hare repeatedly y feet/minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while tortoise < hare or minutes == 0:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes
"""
Implement the classic Fizz Buzz sequence. The fizzbuzz function takes a positive integer n and prints out a single line for each integer from 1 to n. For each i:

If i is divisible by both 3 and 5, print fizzbuzz.
If i is divisible by 3 (but not 5), print fizz.
If i is divisible by 5 (but not 3), print buzz.
Otherwise, print the number i.
Try to make your implementation of fizzbuzz concise.
"""
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"
    for i in range(1, n+1):
        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        print(False)
    else:
        for i in range(2, n//2+1):
          if(n % i == 0):
              print(False)
              break
          elif(i == n//2) :
              print(True)

def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    ans = 0
    for i in range(0, 10):
        if has_digit(n, i):
            ans+=1
    return ans

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    if n % 10 == k:
        return True
    if n >= 10:
        return has_digit(n//10, k)
    return False

def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False
    """
    "*** YOUR CODE HERE ***"
    largest = x%10
    while x!=0:
        x //= 10
        if largest < x%10:
            return(False)
            #return False
    if x == 0:
        return(True)
        #return True
