def solve():

    answer = 0
    return answer


spans1 = ["s1 0 API_GW 10 100", "s2 s1 AUTH 20 40", "s3 s1 DB 50 90"]

spans2 = ["1 0 WEB 0 50", "2 1 DB 10 20", "3 1 DB 30 40"]

# 깊이가 3단계인 엣지 케이스
spans3 = ["root 0 FRONT 0 100", "child1 root BACKEND 10 90", "child2 child1 DB 20 50"]

print(f"Test 1: {solve(spans1)}")
# Expected: ['DB 40', 'API_GW 30', 'AUTH 20']

print(f"Test 2: {solve(spans2)}")
# Expected: ['WEB 30', 'DB 20']

print(f"Test 3: {solve(spans3)}")
# Expected: ['BACKEND 40', 'DB 30', 'FRONT 20']
# 해설:
# DB 총시간 = 30 (순수 30)
# BACK 총시간 = 80 -> 순수 = 80 - 30(DB) = 50
# FRONT 총시간 = 100 -> 순수 = 100 - 80(BACK) = 20
