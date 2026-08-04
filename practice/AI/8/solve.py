def solve(reqs, M):
    if sum(reqs) <= M:
        return max(reqs)
    
    min_num = 0
    max_num = max(reqs)
    
    best = 0
    
    while min_num <= max_num:
        mid = (min_num + max_num) // 2
        total = 0
        for req in reqs:
            total += min(req, mid)
        
        if total <= M:
            best = mid
            min_num = mid + 1
        
        else:
            max_num = mid - 1
        # print (best)  

    answer = best
    return answer


# --- 테스트 실행 영역 ---
req1 = [120, 110, 140, 150]
M1 = 485

req2 = [70, 80, 55]
M2 = 250

req3 = [10, 20, 30, 40]
M3 = 30

print(f"Test 1: {solve(req1, M1)} (Expected: 127)")
print(f"Test 2: {solve(req2, M2)} (Expected: 80)")
print(f"Test 3: {solve(req3, M3)} (Expected: 7)")
# Test 3 흐름: 예산이 극도로 적은 경우. 상한액 7 적용 시 7+7+7+7 = 28 <= 30
