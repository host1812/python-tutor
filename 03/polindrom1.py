'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(s):
    s = s.lower()
    r_offset = 0
    l_offset = 1
    i = 0
    while i <= len(s)//2:
        
        if s[i+r_offset] not in "abcdefghijklmnopqrstuvwxyz":
            # print(f"{s[i+r_offset]} is not alpha -> increasing r_offset")
            r_offset += 1
            continue
        
        if s[-i-l_offset] not in "abcdefghijklmnopqrstuvwxyz":
            # print(f"{s[-i-l_offset]} is not alpha -> increasing l_offset")
            l_offset += 1
            continue

        # print(f"{s[i+r_offset]} == {s[-i-l_offset]}")
        if s[i+r_offset] != s[-i-l_offset]: return False
        i += 1
    return True

def is_palindrome2(s):
    s = [c.lower() for c in s if c.lower() in "abcdefghijklmnopqrstuvwxyz"]
    # print(f"{s} == {s[::-1]}")
    if s != s[::-1]: return False
    return True

# print(f"'testing' is polindrom? {is_palindrome('testing')}")
# print(f"'tacocat' is polindrom? {is_palindrome('tacocat')}")
# print(f"'hannah' is polindrom? {is_palindrome('hannah')}")
# print(f"'r obe rt!' is polindrom? {is_palindrome('r obe rt!')}")
# print(f"'aa bb bb aa!' is polindrom? {is_palindrome('aa bb bb aa!')}")
# print(f"'amanaplanacanalpanama' is polindrom? {is_palindrome('amanaplanacanalpanama')}")
# print(f"'A man, a plan, a canal, Panama!' is polindrom? {is_palindrome('A man, a plan, a canal, Panama!')}")
# print(f"'A man, a plan, a canal, Panama!' is polindrom? {is_palindrome2('A man, a plan, a canal, Panama!')}")

import timeit
# print(timeit.timeit('is_palindrome("A man, a plan, a canal, Panama!")',globals=globals()))
print(timeit.timeit('is_palindrome2("A man, a plan, a canal, Panama!")',globals=globals()))
