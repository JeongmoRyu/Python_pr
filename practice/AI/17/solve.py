def solve():
    answer = 0
    return answer


targets1 = ["OOM", "502"]
logs1 = ["1 502", "3 OOM", "5 INFO", "8 502", "9 502", "10 OOM"]

targets2 = ["DB_ERR", "TIMEOUT"]
logs2 = ["100 TIMEOUT", "200 DB_ERR", "300 TIMEOUT"]

targets3 = ["A", "B", "C"]
logs3 = ["1 A", "5 B", "10 D", "15 E"]

print(f"Test 1: {solve(targets1, logs1)} (Expected: 1)")
# 해설: T=9(502) ~ T=10(OOM) 구간이 시간 차이 1로 가장 짧음

print(f"Test 2: {solve(targets2, logs2)} (Expected: 100)")
# 해설: 100~200 (차이 100) 또는 200~300 (차이 100)

print(f"Test 3: {solve(targets3, logs3)} (Expected: -1)")
