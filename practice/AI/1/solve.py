from collections import deque


def solve():

    answer = 0
    return answer


models1 = ["modelA 10 20", "modelB 5 5"]
logs1 = ["14:00 u1 modelA 500 600", "08:30 u2 modelA 300 100"]

models2 = ["basic 1 1"]
logs2 = [
    "09:00 user1 basic 500 500",
    "18:00 user1 basic 50 50",
    "12:00 user2 basic 10 10",
]

print(f"Test 1: {solve(models1, logs1)}")
# Expected: ['u1 18360', 'u2 5000']

print(f"Test 2: {solve(models2, logs2)}")
# Expected: ['user1 1180', 'user2 24']
