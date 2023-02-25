# Brute_force_pattern_pr

```python
target = 'abacdabcdabcabcdef'
pattern = 'abcdef'

# BF - for
# target에 pattern이 어디에 있는지를 찾는 함수
def brute_force_for(target, pattern):
    target_len = len(target)
    pattern_len = len(pattern)
    # 범위 설정을 해준다.
    for i in range(target_len - pattern_len + 1):
        # 패턴길이가 남는 인덱스까지 검사
        # 패턴과 어디까지 일치했었는지(어는 정도의 길이가 일치하는지)
        count = 0
        for j in range(pattern_len):
            # 패턴과 일치하지 않는다.
            if target[i + j] != pattern[j]:
                break
            else:
                count += 1
        # 일치한 pattern의 글자 수가 pattern의 총 글자 수 보다 크거나 같다.
        if count >= pattern_len:
            return i

    # 못 찾을때
    return -1

print(brute_force_for(target, pattern))

```

```python
target = 'abacdabcdabcabcdef'
pattern = 'abcdef'

def brute_force_for2(target, pattern):
    target_length = len(target)
    pattern_length = len(pattern)
    # i는 타겟 검사용 index
    # j는 패턴 검사용 index
    i = j = 0
    # 1. j >= pattern_length -> 성공
    # 2. i >= target_length -> 실패
    while j < pattern_length and i < target_length:
        if target[i] != pattern[j]:
            # BF의 방식대로 일치하기 시작한 지점 바로 다음 지점으로
            i = i - j
            # 다음은 0이어야하기 때문에 -1
            j = -1
        # 다음 순회 준비
        i += 1
        j += 1
    if j == pattern_length:
        # 어디까지 갔는지 - 찾는 것의 길이
        return i - pattern_length
    else:
        return -1

print(brute_force_for2(target, pattern))
```