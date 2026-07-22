def solve():

    answer = 0
    return answer


N1 = 4
times1 = [10, 20, 10, 20]
deps1 = [[1, 2], [1, 3], [2, 4], [3, 4]]

N2 = 3
times2 = [5, 5, 5]
deps2 = []

N3 = 5
times3 = [10, 10, 20, 20, 30]
deps3 = [[1, 3], [2, 3], [3, 4], [4, 5]]

print(f"Test 1: {solve(N1, times1, deps1)} (Expected: 50)")
print(f"Test 2: {solve(N2, times2, deps2)} (Expected: 5)")
print(f"Test 3: {solve(N3, times3, deps3)} (Expected: 80)")
