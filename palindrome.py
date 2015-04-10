'''
Write an efficient function that checks whether any permutation of an input string is a palindrome.
Examples:

"civic" should return true
"ivicc" should return true
"civil" should return false
"livci" should return false
'''
from collections import defaultdict


def is_any_perm_palindrome(test_string):
    # count occurances of each character
    d = defaultdict(int)
    for c in test_string:
        d[c] += 1
    odd_counter = 0
    for k, v in d.items():
        if v % 2 == 1:
            if odd_counter >= 1:
                return False
            odd_counter += 1
    if odd_counter > 1:
        return False
    return True


def test():
    try:
        if not is_any_perm_palindrome("civic"):
            raise Exception("Test Failed")
        if not is_any_perm_palindrome("ivicc"):
            raise Exception("Test Failed")
        if is_any_perm_palindrome("civil"):
            raise Exception("Test Failed")
        if is_any_perm_palindrome("livic"):
            raise Exception("Test Failed")
        if not is_any_perm_palindrome("i"):
            raise Exception("Test Failed")
        if not is_any_perm_palindrome("iii"):
            raise Exception("Test Failed")
        if not is_any_perm_palindrome("iiii"):
            raise Exception("Test Failed")
        print "Tests passed"
    except Exception, e:
        print e

test()
