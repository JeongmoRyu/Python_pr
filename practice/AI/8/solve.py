def solve():

    answer = 0
    return answer


# --- 테스트 실행 영역 ---
req1 = [120, 110, 140, 150]
M1 = 485

req2 = [70, 80, 55]
M2 = 250

req3 = [10, 20, 30, 40]
M3 = 30

print(f"Test 1: {solution(req1, M1)} (Expected: 127)")
print(f"Test 2: {solution(req2, M2)} (Expected: 80)")
print(f"Test 3: {solution(req3, M3)} (Expected: 7)")
# Test 3 흐름: 예산이 극도로 적은 경우. 상한액 7 적용 시 7+7+7+7 = 28 <= 30
