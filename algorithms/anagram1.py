import unittest

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    if sorted(s1.replace(" ", "").lower()) != sorted(s2.replace(" ", "").lower()):
        return False

    return True

def is_anagram2(s1, s2):
    if len(s1) != len(s2):
        return False

    storage = {}
    for i in range(len(s1)):
        char1 = s1[i].lower()
        if char1 not in storage and char1 != " ":
            storage[char1] = 1
        else:
            storage[char1] += 1
        
        char2 = s2[i].lower()
        if char2 not in storage and char2 != " ":
            storage[char2] = -1
        else:
            storage[char2] -= 1

    for k,v in storage.items():
        if v != 0: return False

    return True

class TestAnagram(unittest.TestCase):
    def test_simple_anagram(self):
        self.assertTrue(is_anagram("Debit card", "Bad credit"))

    def test_simple_anagram2(self):
        self.assertTrue(is_anagram2("Debit card", "Bad credit"))

if __name__ == "__main__":
    unittest.main()
