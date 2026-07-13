from collections import deque



def solve():
  
  answer = 0
  return answer





logs1 = [
    "u1 10:00 FAIL", 
    "u1 10:02 FAIL", 
    "u1 10:04 FAIL", 
    "u2 11:00 SUCCESS"
]

logs2 = [
    "a 23:55 FAIL", 
    "a 23:59 FAIL", 
    "a 00:01 FAIL", 
    "b 10:00 FAIL"
]

logs3 = [
    "bob 09:00 FAIL", 
    "bob 09:03 SUCCESS", 
    "bob 09:04 FAIL", 
    "bob 09:05 FAIL", 
    "bob 09:08 FAIL"
]

logs4 = [
    "test 14:05 FAIL",
    "test 14:01 FAIL",
    "test 14:03 FAIL",
    "safe 15:00 FAIL"
]

print(f"Test 1: {solve(logs1)} (Expected: ['u1'])")
print(f"Test 2: {solve(logs2)} (Expected: [])")
print(f"Test 3: {solve(logs3)} (Expected: ['bob'])")
print(f"Test 4: {solve(logs4)} (Expected: ['test'])")