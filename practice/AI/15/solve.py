def solve():
    answer = 0
    return answer

N1, K1 = 2, 5
logs1 = ["1 S", "2 F", "3 F", "4 S", "8 S", "9 S"]

N2, K2 = 2, 5
logs2 = ["10 F", "11 F", "15 S", "16 F", "20 S", "21 S"]

print(f"Test 1: {solve(N1, K1, logs1)}")
# Expected: ['SUCCESS', 'FAIL', 'FAIL', 'DROPPED', 'SUCCESS', 'SUCCESS']

print(f"Test 2: {solve(N2, K2, logs2)}")
# Expected: ['FAIL', 'FAIL', 'DROPPED', 'FAIL', 'DROPPED', 'SUCCESS']
