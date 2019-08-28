def interleave(s1, s2):
    return "".join(["".join(x) for x in list(zip(s1, s2))])

result = interleave("aaa", "zzz")

print(result)