class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

def solve(words, queries):
    root = TrieNode()
    
    for word in words:
        curr  = root
        curr.count += 1
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.count += 1
    
    result = []
    for query in queries:
        curr  = root
        found = True
        
        for char in query:
            if char not in curr.children:
                found = False
                break
            curr = curr.children[char]
        
        if found:
            result.append(curr.count)
        else:
            result.append(0)

    answer = result
    return answer


# --- 테스트 실행 영역 ---
words1 = ["prompt", "pro", "project", "program", "test"]
queries1 = ["pro", "pr", "test", "a"]

words2 = ["ai", "api", "app", "apple"]
queries2 = ["a", "ap", "b"]

print(f"Test 1: {solve(words1, queries1)} (Expected: [4, 4, 1, 0])")
print(f"Test 2: {solve(words2, queries2)} (Expected: [4, 3, 0])")
