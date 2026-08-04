def solve():
    answer = 0
    return answer


cap1, ref1 = 10, 2
req1 = [[1, 5], [1, 6], [2, 3], [5, 10]]

cap2, ref2 = 5, 1
req2 = [[2, 5], [3, 2], [10, 5]]

print(f"Test 1: {solve(cap1, ref1, req1)}")
# Expected: ['200', '429', '200', '200']

print(f"Test 2: {solve(cap2, ref2, req2)}")
# Expected: ['200', '429', '200']
