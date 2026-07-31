def solve():
    answer = 0
    return answer

routes1 = [
    "/api/v1/auth auth_svc 2",
    "/api/v1/auth/admin admin_svc 1",
    "/api/v2 legacy 3",
]
reqs1 = [
    "/api/v1/auth/login",
    "/api/v1/auth/logout",
    "/api/v1/auth/admin/settings",
    "/api/v3/info",
    "/api/v1/auth/profile",
]

routes2 = ["/ route 1", "/img image 2"]
reqs2 = ["/img/logo.png", "/index.html", "/img/bg.png"]

print(f"Test 1: {solve(routes1, reqs1)}")
# Expected: ['auth_svc-1', 'auth_svc-2', 'admin_svc-1', '404', 'auth_svc-1']

print(f"Test 2: {solve(routes2, reqs2)}")
# Expected: ['image-1', 'route-1', 'image-2']
