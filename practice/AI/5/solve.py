from collections import defaultdict, deque
"""
-------------------------------------------------------------
"""
def solve(N, times, deps):
    graph = defaultdict(list)
    indegree = [0] * (N + 1)
    
    for a, b in deps:
        graph[a].append(b)
        indegree += 1

    dp = [0] * (N+1)
    for i in range(1, N+1):
        dp[i] = times[i-1]
        
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        cur = q.popleft()
        
        for next in graph[cur]:
            dp[next] = max(dp[next], dp[cur] + times[next - 1])
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    
    

    answer = max(dp[1:])
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
