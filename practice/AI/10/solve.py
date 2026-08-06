def solve(threshold, data):
    
    if not data:
        return []
    
    first_t, first_v = map(int, data[0].split())
    last_t = first_t
    last_v = first_v
    
    result = [first_v]
    
    for i in range(1, len(data)):
        t, v = map(int, data[i].split())
        
        while last_t + 1 < t:
            last_t += 1
            result.append(last_v)
        
        if abs(v - last_v) > threshold:
            curr = last_v
        else:
            curr = v
            last_v = v
        
        result.append(curr)
        last_t = t
    answer = result
    return answer











threshold1 = 5
data1 = ["1 10", "2 12", "4 15", "5 30", "6 14"]

threshold2 = 10
data2 = ["10 50", "13 52", "14 80", "15 55"]

# 간격이 매우 큰 엣지 케이스
threshold3 = 3
data3 = ["1 0", "5 2", "6 10"]

print(f"Test 1: {solve(threshold1, data1)}")
# Expected: [10, 12, 12, 15, 15, 14]

print(f"Test 2: {solve(threshold2, data2)}")
# Expected: [50, 50, 50, 52, 52, 55]

print(f"Test 3: {solve(threshold3, data3)}")
# Expected: [0, 0, 0, 0, 2, 2]
# (T=1:0, T=2:0, T=3:0, T=4:0, T=5:2(정상), T=6:10(이상치->2))
