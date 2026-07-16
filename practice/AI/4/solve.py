def solve():

    answer = 0
    return answer

users1 = [
    "u1 1.1.1 010-1111",
    "u2 2.2.2 010-1111",
    "u3 1.1.1 010-2222",
    "u4 3.3.3 010-3333",
]

users2 = ["a 1.2.3 010-0000", "b 1.2.3 010-0000", "c 4.5.6 010-1234"]

print(f"Test 1: {solve(users1)} (Expected: [2, 3])")
print(f"Test 2: {solve(users2)} (Expected: [2, 2])")
