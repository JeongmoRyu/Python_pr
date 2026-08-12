def solve():
    answer = 0
    return answer


logs1 = ["1 PUT a 10", "2 PUT b 20 3", "3 DELETE a", "4 PUT c 30 5"]
curr1 = 5

logs2 = ["10 PUT s1 tA 50", "20 PUT s2 tB", "30 PUT s1 tC", "40 DELETE s2"]
curr2 = 50

print(f"Test 1: {solve(logs1, curr1)} (Expected: ['c 30'])")
print(f"Test 2: {solve(logs2, curr2)} (Expected: ['s1 tC'])")
# 해설 Test 2: s1은 처음에 TTL이 있었으나, T=30에서 TTL 없는 PUT으로 덮어씌워져 영구 보존됨.
