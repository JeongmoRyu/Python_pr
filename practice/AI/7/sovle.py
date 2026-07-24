def solve():

    answer = 0
    return answer

# --- 테스트 실행 영역 ---
temps1 = [70, 72, 85, 80, 90, 75]
W1 = 3
limit1 = 85

temps2 = [50, 55, 53, 52, 51]
W2 = 2
limit2 = 60

# 내림차순으로 온도가 떨어지는 엣지 케이스
temps3 = [100, 90, 80, 70, 60]
W3 = 3
limit3 = 85

print(f"Test 1: {solve(temps1, W1, limit1)} (Expected: [0, 1, 2, 3])")
print(f"Test 2: {solve(temps2, W2, limit2)} (Expected: [])")
print(f"Test 3: {solve(temps3, W3, limit3)} (Expected: [0])")
# Test 3 흐름: [100, 90, 80] 최고 100(기록), [90, 80, 70] 최고 90(기록), [80, 70, 60] 최고 80(미달) -> [0, 1] 반환
