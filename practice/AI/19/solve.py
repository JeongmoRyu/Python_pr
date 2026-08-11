def solve():
    answer = 0
    return answer


M1 = 360
servers1 = ["s1 45", "s2 135", "s3 225"]
requests1 = ["req1 10", "req2 100", "req3 200", "req4 300"]

M2 = 1000
servers2 = ["nodeA 900", "nodeB 100"]
requests2 = ["k1 50", "k2 150", "k3 800", "k4 950"]

print(f"Test 1: {solve(M1, servers1, requests1)} (Expected: ['s1', 's2', 's3', 's1'])")
print(
    f"Test 2: {solve(M2, servers2, requests2)} (Expected: ['nodeB', 'nodeA', 'nodeA', 'nodeB'])"
)
