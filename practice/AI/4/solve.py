from collections import defaultdict, deque

def solve(users):
    ips = defaultdict(list)
    tels = defaultdict(list)
    user_list = []
    
    for i, user in enumerate(users):
        id, ip, tel = user.split()
        user_list.append((id, ip))
        ips[ip].append(i)
        tels[tel].append(i)
    
    visited = [0]*len(users)
    total = 0
    max_group_size = 0
    
    for i in range(len(users)):
        if not visited[i]:
            total += 1
            current = 0
            
            q = deque([i])
            visited[i] = 1
            
            while q:
                cur = q.popleft()
                current += 1
                
                cur_ip, cur_tel = user_list[cur]
                
                for j in ips[cur_ip]:
                    if not visited[j]:
                        visited[j] = 1
                        q.append(j)
                
                for k in tels[cur_tel]:
                    if not visited[k]:
                        visited[k] = 1
                        q.append(k)
            if current > max_group_size:
                max_group_size = current
    
    

    answer = [total, max_group_size]
    return answer


users1 = [
    "u1 1.1.1 010-1111",
    "u2 2.2.2 010-1111",
    "u3 1.1.1 010-2222",
    "u4 3.3.3 010-3333",
]

users2 = ["a 1.2.3 010-0000", "b 1.2.3 010-0000", "c 4.5.6 010-1234"]

print(f"Test 1: {solve(users1)} (Expected: [2, 3])")
print(f"Test 2: {solve(users2)} (Expected: [2, 2])")
