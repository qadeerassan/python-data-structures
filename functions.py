"""
----------------------------------------------------
functions.py
Holds functions.
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-02-05"
----------------------------------------------------
"""
def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Preconditions:
        x - an integer (int)
        y - an integer (int)
    Postconditions:
        returns
        ans - the function result (int)
    -------------------------------------------------------
    """
    #base case
    if x < 0 or y < 0:
        ans = x - y
    else:
        ans = recurse(x-1, y) + recurse(x, y-1)
    return ans

def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Preconditions:
        n - an integer (int)
        m - an integer (int)
    Postconditions:
        returns
        ans - the function result (int)
    -------------------------------------------------------
    """
    if m % n == 0:
        ans = n
    else:
        ans = gcd(m, (m % n))
    return ans

def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Preconditions:
        s - string to examine (str)
    Postconditions:
        returns
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    vowels = "aeiouAEIOU"
    count = 0
    
    if s == "":
        count = 0
    elif s[0] in vowels:
        count = 1 + vowel_count(s[1:])
    else:
        count = vowel_count(s[1:])
    return count

def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Preconditions:
        base - base to apply power to (float)
        power - power to apply (int)
    Postconditions:
        returns
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    if power == 0:
        ans = 1
    elif power == 1:
        ans = base
    elif power > 0:
        ans = base * to_power(base, power - 1)
    elif power < 0:
        ans = 1 / (base * to_power(base, -power - 1))
    return ans

def palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: is_palindrome = palindrome(s)
    -------------------------------------------------------
    Preconditions:
        s - a string (str)
    Postconditions:
        returns
        is_palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    if len(s) < 2:
        is_palindrome = True
    elif s[0].isalpha() != True:
        is_palindrome = palindrome(s[1:])
    elif s[-1].isalpha() != True:
        is_palindrome = palindrome(s[-1:])
    elif s[0] == s[-1]:
        is_palindrome = palindrome(s[1:-1])
    else:
        is_palindrome = False
    return is_palindrome

def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Preconditions:
        bag - a list of values (list)
    Postconditions:
        returns
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """
    new_set = [] 
    if bag == []:
        new_set = [] 
    elif bag[0] not in bag[1:]:
        new_set = [bag[0]] + bag_to_set(bag[1:])
    else:
        new_set = bag_to_set(bag[1:])
    return new_set
    