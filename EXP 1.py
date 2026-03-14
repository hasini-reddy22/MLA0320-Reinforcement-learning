import numpy as np
import random

# Grid size
GRID_SIZE = 5

# Actions
actions = ["UP", "DOWN", "LEFT", "RIGHT"]

# Dirt locations (+1 reward)
dirt_cells = [(1,2), (3,3), (4,1)]

# Obstacles (-1 penalty)
obstacles = [(2,2), (3,1)]

# Initialize grid rewards
grid = np.zeros((GRID_SIZE, GRID_SIZE))

for d in dirt_cells:
    grid[d] = 1

for o in obstacles:
    grid[o] = -1

# Start position
start_state = (0,0)


# Function to move robot
def move(state, action):
    r, c = state

    if action == "UP":
        r = max(r-1, 0)
    elif action == "DOWN":
        r = min(r+1, GRID_SIZE-1)
    elif action == "LEFT":
        c = max(c-1, 0)
    elif action == "RIGHT":
        c = min(c+1, GRID_SIZE-1)

    return (r, c)


# Random Policy
def random_policy(state):
    return random.choice(actions)


# Greedy Policy (move towards dirt)
def greedy_policy(state):
    r, c = state

    # Find nearest dirt
    if len(dirt_cells) == 0:
        return random.choice(actions)

    target = dirt_cells[0]
    tr, tc = target

    if tr > r:
        return "DOWN"
    if tr < r:
        return "UP"
    if tc > c:
        return "RIGHT"
    if tc < c:
        return "LEFT"

    return random.choice(actions)


# Simulation
def simulate(policy, steps=20):

    state = start_state
    total_reward = 0

    print("Start:", state)

    for i in range(steps):

        action = policy(state)
        next_state = move(state, action)

        reward = grid[next_state]
        total_reward += reward

        print(f"Step {i+1}: {state} -> {action} -> {next_state} | Reward: {reward}")

        state = next_state

    print("Total Reward:", total_reward)


# Run simulations
print("\n--- Random Policy Simulation ---")
simulate(random_policy)

print("\n--- Greedy Policy Simulation ---")
simulate(greedy_policy)
