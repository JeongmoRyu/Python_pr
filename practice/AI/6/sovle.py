from collections import OrderedDict
"""
orderdict
move_to_end(id)
popitem
popitem(last=False)
"""
def solve(cap, reqs):
    cache = OrderedDict()
    current = 0
    total = 0
    
    for req in reqs:
        id, token_str = req.split()
        token = int(token_str)
        if id in cache:
            total += 1
            cache.move_to_end(id)
        else:
            total += token
            
            if token > cap:
                continue
                
            while current + token > cap:
                _, end_token = cache.popitem(last=False)
                current -= end_token
            
            cache[id] = token
            current += token
            

    answer = total
    return answer


cap1 = 100
req1 = ["A 40", "B 50", "A 40", "C 30", "B 50"]

cap2 = 50
# Y는 60으로 캐시 용량(50)을 초과하므로 저장되지 않고 패스되어야 함
req2 = ["X 30", "Y 60", "X 30"]

print(f"Test 1: {solve(cap1, req1)} (Expected: 171)")
print(f"Test 2: {solve(cap2, req2)} (Expected: 91)")
# Test 2 흐름: X(미스:30) -> Y(미스:60, 캐시 안됨) -> X(히트:1) = 91
