def solve():

    answer = 0
    return answer

K1 = 5
logs1 = ["10:00:00 10", "10:00:05 15", "10:00:09 5", "10:00:15 10"]

K2 = 0
logs2 = ["09:00:00 30", "09:00:15 20", "09:00:25 15", "09:00:30 10"]

# 시간순으로 정렬되지 않은 엣지 케이스
K3 = 10
logs3 = ["13:00:20 10", "13:00:00 10", "13:00:10 10"]

print(f"Test 1: {solve(K1, logs1)} (Expected: 3)")
print(f"Test 2: {solve(K2, logs2)} (Expected: 3)")
print(f"Test 3: {solve(K3, logs3)} (Expected: 2)")
