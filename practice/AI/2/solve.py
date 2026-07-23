def solve(models, logs):

    rates = {}
    for model in models:
        name, p_cost, c_cost = model.split()
        rates[name] = (int(p_cost), int(c_cost))
    user_cost = {}
    
    for log in logs:
        time, user_id, model_name, p_token, c_token = log.split()
        p_tok = int(p_token)
        c_tok = int(c_token)
        
        p_rate, c_rate = rates[model_name]
        cost = p_rate*p_tok + c_rate*c_tok
        
        if p_tok + c_tok >= 1000:
            cost = int(cost*0.9)
        
        h, m  = map(int, time.split(":"))
        minutes = h * 60 + m
        if 9 * 60 <= minutes < 18*60:
            cost = int(cost * 1.2)
        
        if user_id not in user_cost:
            user_cost[user_id] = 0
        user_cost[user_id] += cost
    
    answer = []
    for user_id in sorted(user_cost.keys()):
        answer.append(f"{user_id} {user_cost[user_id]}")


    
    return answer


models1 = ["modelA 10 20", "modelB 5 5"]
logs1 = [
    "14:00 u1 modelA 500 600", 
    "08:30 u2 modelA 300 100"
]

models2 = ["basic 1 1"]
logs2 = [
    "09:00 user1 basic 500 500", 
    "18:00 user1 basic 50 50",
    "12:00 user2 basic 10 10"
]

# print(f"Test 1: {solve(models1, logs1)}")
# Expected: ['u1 18360', 'u2 5000']

print(f"Test 2: {solve(models2, logs2)}")
# Expected: ['user1 1180', 'user2 24']
