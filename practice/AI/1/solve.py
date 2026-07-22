from collections import defaultdict, deque


def solve(log_list):
    logs = defaultdict(list)

    for log in log_list:
        user_id, time, status = log.split()
        h, m = map(int, time.split(":"))
        minutes = h*60 + m
        logs[user_id].append((minutes ,status))
        
    locked_users = []

    for user_id, records in logs.items():
        records.sort(key=lambda x : x[0])

        fail_num = deque()
        locked = False
        
        for time, status in records:
            if status == "SUCCESS":
                fail_num.clear()
            else:
                fail_num.append(time)

                while fail_num and (time - fail_num[0]) > 5:
                    fail_num.popleft()
                if len(fail_num) >= 3:
                    locked = True
                    break
        
        if locked:
            locked_users.append(user_id)

    answer = sorted(locked_users)
    return answer

logs1 = [
    "u1 10:00 FAIL", 
    "u1 10:02 FAIL", 
    "u1 10:04 FAIL", 
    "u2 11:00 SUCCESS"
]

# 테스트 케이스 2: 자정 넘어가는 경우 (단순 계산 시 5분 이내가 아님)
logs2 = [
    "a 23:55 FAIL", 
    "a 23:59 FAIL", 
    "a 00:01 FAIL", 
    "b 10:00 FAIL"
]

# 테스트 케이스 3: 중간에 SUCCESS가 섞여 있어 카운트가 초기화되는 경우
logs3 = [
    "bob 09:00 FAIL", 
    "bob 09:03 SUCCESS", 
    "bob 09:04 FAIL", 
    "bob 09:05 FAIL", 
    "bob 09:08 FAIL"
]

# 테스트 케이스 4: 시간순으로 정렬되어 있지 않은 로그 (정렬 로직 검증)
logs4 = [
    "test 14:05 FAIL",
    "test 14:01 FAIL",
    "test 14:03 FAIL",
    "safe 15:00 FAIL"
]

# 테스트 결과 출력
# print(f"Test 1: {solve(logs1)} (Expected: ['u1'])")
# print(f"Test 2: {solve(logs2)} (Expected: [])")
# print(f"Test 3: {solve(logs3)} (Expected: ['bob'])")
print(f"Test 4: {solve(logs4)} (Expected: ['test'])")

