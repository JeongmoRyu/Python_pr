def solve():

    answer = 0
    return answer


# --- 테스트 실행 영역 ---
words1 = ["prompt", "pro", "project", "program", "test"]
queries1 = ["pro", "pr", "test", "a"]

words2 = ["ai", "api", "app", "apple"]
queries2 = ["a", "ap", "b"]

print(f"Test 1: {solve(words1, queries1)} (Expected: [4, 4, 1, 0])")
print(f"Test 2: {solve(words2, queries2)} (Expected: [4, 3, 0])")
