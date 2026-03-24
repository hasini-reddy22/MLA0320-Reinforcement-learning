import numpy as np

# Grid setup
GRID_SIZE = 6
ACTIONS = ['U', 'D', 'L', 'R']
ACTION_DELTA = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

GAMMA = 0.9  # discount factor
THETA = 1e-4  # convergence threshold

# Define delivery points
delivery_points = [(0, 5), (5, 5)]
warehouse = (0, 0)

# Initialize rewards
rewards = np.full((GRID_SIZE, GRID_SIZE), -1.0)
for d in delivery_points:
    rewards[d] = 50.0

# Initialize policy randomly
policy = np.random.choice(ACTIONS, size=(GRID_SIZE, GRID_SIZE))

# Initialize value function
V = np.zeros((GRID_SIZE, GRID_SIZE))


def get_next_state(state, action):
    x, y = state
    dx, dy = ACTION_DELTA[action]
    nx, ny = x + dx, y + dy
    
    # Stay in bounds
    if nx < 0 or nx >= GRID_SIZE or ny < 0 or ny >= GRID_SIZE:
        return state
    return (nx, ny)


def policy_evaluation(policy, V):
    while True:
        delta = 0
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                state = (i, j)
                action = policy[i, j]
                next_state = get_next_state(state, action)
                
                v = rewards[next_state] + GAMMA * V[next_state]
                delta = max(delta, abs(v - V[i, j]))
                V[i, j] = v
        
        if delta < THETA:
            break
    return V


def policy_improvement(policy, V):
    policy_stable = True
    
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            state = (i, j)
            old_action = policy[i, j]
            
            action_values = {}
            for action in ACTIONS:
                next_state = get_next_state(state, action)
                action_values[action] = rewards[next_state] + GAMMA * V[next_state]
            
            best_action = max(action_values, key=action_values.get)
            policy[i, j] = best_action
            
            if old_action != best_action:
                policy_stable = False
    
    return policy, policy_stable


def policy_iteration():
    global policy, V
    
    while True:
        V = policy_evaluation(policy, V)
        policy, stable = policy_improvement(policy, V)
        
        if stable:
            break
    
    return policy, V


# Run algorithm
optimal_policy, optimal_values = policy_iteration()

print("Optimal Policy:")
print(optimal_policy)

print("\nOptimal Value Function:")
print(optimal_values)
