import numpy as np

# Grid size
GRID_SIZE = 5

# Actions
ACTIONS = ['U', 'D', 'L', 'R']
ACTION_DELTA = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

# Parameters
GAMMA = 0.9
THETA = 1e-4

# Pick-up points (goal states)
pickup_points = [(0, 4), (4, 4)]

# Rewards
rewards = np.full((GRID_SIZE, GRID_SIZE), -1.0)
for p in pickup_points:
    rewards[p] = 100.0

# Initialize value function
V = np.zeros((GRID_SIZE, GRID_SIZE))


def get_next_state(state, action):
    x, y = state
    dx, dy = ACTION_DELTA[action]
    nx, ny = x + dx, y + dy
    
    # Boundary check
    if nx < 0 or nx >= GRID_SIZE or ny < 0 or ny >= GRID_SIZE:
        return state
    return (nx, ny)


def value_iteration():
    global V
    
    while True:
        delta = 0
        new_V = np.copy(V)
        
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                state = (i, j)
                
                # If it's a terminal state (pickup), skip update
                if state in pickup_points:
                    continue
                
                action_values = []
                for action in ACTIONS:
                    next_state = get_next_state(state, action)
                    value = rewards[next_state] + GAMMA * V[next_state]
                    action_values.append(value)
                
                best_value = max(action_values)
                new_V[i, j] = best_value
                
                delta = max(delta, abs(best_value - V[i, j]))
        
        V = new_V
        
        if delta < THETA:
            break


def extract_policy():
    policy = np.empty((GRID_SIZE, GRID_SIZE), dtype=str)
    
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            state = (i, j)
            
            if state in pickup_points:
                policy[i, j] = 'G'  # Goal
                continue
            
            action_values = {}
            for action in ACTIONS:
                next_state = get_next_state(state, action)
                action_values[action] = rewards[next_state] + GAMMA * V[next_state]
            
            best_action = max(action_values, key=action_values.get)
            policy[i, j] = best_action
    
    return policy


# Run value iteration
value_iteration()
optimal_policy = extract_policy()

print("Optimal Value Function:\n", V)
print("\nOptimal Policy:\n", optimal_policy)
