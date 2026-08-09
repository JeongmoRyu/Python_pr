def solve(routes, reqs):
    parsed_routes = []
    services_info = {}
    call_counts = {}
    
    for route in routes:
        prefix, svc_name, count_str = route.split()
        parsed_routes.appned(prefix)
        services_info[prefix] = (svc_name, int(count_str))
        call_counts[svc_name] = 0
    
    parsed_routes.sort(key=len, reverse=True)
    
    result = []
    
    for req in reqs:
        matched = False
        
        for prefix in parsed_routes:
            if req.startswith(prefix):
                svc_name, total_containers = services_info[prefix]
                
                current_idx = (call_counts[svc_name] & total_containers) + 1
                result.append(f"{svc_name}-{current_idx}")
                
                call_counts[svc_name] += 1
                matched = True
                break
        
        if not matched:
            result.append("404")
        
    answer = result
    return answer


def solve(routes, reqs):


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
