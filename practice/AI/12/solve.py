def solve(logs):
    event = []
    for start, end in logs:
        event.append((start, 1))
        event.append((end + 1, -1))
    
    event.sort(key=lambda x: (x[0], x[1]))
    
    max_users = 0
    curr = 0
    
    for time, diff in event:
        curr += diff
        if curr > max_users:
            max_users = curr
    
    
    answer = max_users
    return answer


logs1 = [[1, 5], [2, 6], [5, 8], [9, 10]]
logs2 = [[10, 20], [25, 30], [5, 10], [15, 20]]
logs3 = [[1, 1000000000], [500000000, 1000000000]]  # 시간이 매우 큰 엣지 케이스

print(f"Test 1: {solve(logs1)} (Expected: 3)")
# Test 1 흐름: T=5에 들어오는 사람(1)과 T=6에 나가는 사람(-1)이 처리됨. T=5일 때 3명 도달.

print(f"Test 2: {solve(logs2)} (Expected: 2)")
# Test 2 흐름: [5,10], [10,20], [15,20] -> T=10에 두 명 중첩, T=15에 두 명 중첩 (최대 2)

print(f"Test 3: {solve(logs3)} (Expected: 2)")
