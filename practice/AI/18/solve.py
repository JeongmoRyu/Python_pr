def solve():
    answer = 0
    return answer


jobs1 = [[1, 3, 50], [2, 5, 20], [4, 6, 70], [6, 8, 30]]
jobs2 = [[1, 10, 100], [2, 4, 30], [5, 7, 40], [8, 11, 40]]

# 시작 시간과 종료 시간이 같은 경계값 테스트
jobs3 = [[1, 2, 50], [2, 3, 50], [1, 3, 90]]

print(f"Test 1: {solve(jobs1)} (Expected: 150)")
print(f"Test 2: {solve(jobs2)} (Expected: 110)")
print(f"Test 3: {solve(jobs3)} (Expected: 100)")
# Test 3 해설: [1,2]와 [2,3]을 이어서 실행하면 50+50=100. [1,3] 단일 실행(90)보다 큼.
