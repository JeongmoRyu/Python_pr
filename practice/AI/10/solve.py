def solve():

    answer = 0
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
