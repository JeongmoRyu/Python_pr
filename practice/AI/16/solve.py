def solve():
    answer = 0
    return answer

W1, limit1 = 10, 3
logs1 = ["1 u1", "5 u1", "10 u1", "11 u1", "12 u1", "15 u1"]

W2, limit2 = 5, 2
logs2 = ["1 a", "2 a", "3 b", "4 a", "5 b", "6 a"]

print(f"Test 1: {solve(W1, limit1, logs1)}")
# Expected: ['ACCEPT', 'ACCEPT', 'ACCEPT', 'ACCEPT', 'DROP', 'ACCEPT']

print(f"Test 2: {solve(W2, limit2, logs2)}")
# Expected: ['ACCEPT', 'ACCEPT', 'ACCEPT', 'DROP', 'ACCEPT', 'ACCEPT']
