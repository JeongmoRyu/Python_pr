def solve(N, edges, start, end, K):
    distances = [float('inf')]*N
    distances[start] = 0
    
    for hop in range(K+1):
        temp = distances[:]
        for u, v, w in edges:
            if distances[u] != float('inf') and distances[u] + w < temp[v]:
                temp[v] = distances[u] + w
        
        distances = temp
    
    if distances[end] == float('inf'):
        return -1
    answer = distances[end]
    return answer


N1 = 4
edges1 = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [0, 2, 500]]
start1 = 0
end1 = 3
K1 = 1

N2 = 3
edges2 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
start2 = 0
end2 = 2
K2 = 0

print(f"Test 1: {solve(N1, edges1, start1, end1, K1)} (Expected: 600)")
print(f"Test 2: {solve(N2, edges2, start2, end2, K2)} (Expected: 500)")
