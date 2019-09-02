import unittest

def pair_sum(lst, n):
    result = []
    for x in lst:
        if x > n: continue
        for y in lst:
            if x + y == n and (min(x,y),max(x,y)) not in result:
                result.append((min(x,y),max(x,y)))
    return result

class TestAnagram(unittest.TestCase):
    def test_array_pairsum(self):
        self.assertEqual(pair_sum([1,3,2,2],4), [(1,3),(2,2)])

    def test_array_pairsum2(self):
        self.assertEqual(pair_sum([1,3,2,2,4,0],4), [(1,3),(2,2),(0,4)])

if __name__ == "__main__":
    unittest.main()
