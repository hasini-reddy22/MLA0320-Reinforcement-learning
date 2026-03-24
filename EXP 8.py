import random

# Grid size
N = 6

# Start and goal
start = (0, 0)
goal = (5, 5)

# Intersections (must stop)
intersections = [(2, 2), (3, 3), (1, 4)]

# Actions
ACTIONS = ['U', 'D', 'L', 'R']
DELTA = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}


def next_state(state, action):
    x, y = state
    dx, dy = DELTA[action]
    nx, ny = x + dx, y + dy

    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        return state
    return (nx, ny)


# -----------------------------
# Policies
# -----------------------------

# 1. Naive (ignore rules)
def naive_policy(state):
    x, y = state
    gx, gy = goal

    if x < gx:
        return 'D'
    if y < gy:
        return 'R'
    if x > gx:
        return 'U'
    return 'L'


# 2. Safe (stop at intersections)
def safe_policy(state, stopped):
    if state in intersections and not stopped:
        return 'STOP'

    x, y = state
    gx, gy = goal

    if x < gx:
        return 'D'
    if y < gy:
        return 'R'
    if x > gx:
        return 'U'
    return 'L'


# -----------------------------
# Simulation
# -----------------------------
def simulate(policy_type, max_steps=50):
    state = start
    steps = 0
    total_reward = 0
    stopped = False

    path = [state]

    while state != goal and steps < max_steps:
        if policy_type == "naive":
            action = naive_policy(state)
        else:
            action = safe_policy(state, stopped)

        if action == 'STOP':
            reward = -0.5  # small delay penalty
            stopped = True
        else:
            next_s = next_state(state, action)

            # Traffic violation penalty
            if policy_type == "naive" and state in intersections:
                reward = -10  # penalty for not stopping
            else:
                reward = -1

            state = next_s
            stopped = False

        total_reward += reward
        steps += 1
        path.append(state)

    # Goal reward
    if state == goal:
        total_reward += 100

    return total_reward, steps, path


# -----------------------------
# Run Evaluation
# -----------------------------
def evaluate(policy_type, runs=50):
    total_rewards = 0
    total_steps = 0

    for _ in range(runs):
        r, s, _ = simulate(policy_type)
        total_rewards += r
        total_steps += s

    avg_reward = total_rewards / runs
    avg_steps = total_steps / runs

    return avg_reward, avg_steps


# Evaluate both policies
naive_result = evaluate("naive")
safe_result = evaluate("safe")

print("Naive Policy -> Avg Reward:", round(naive_result[0], 2),
      "Avg Steps:", round(naive_result[1], 2))

print("Safe Policy  -> Avg Reward:", round(safe_result[0], 2),
      "Avg Steps:", round(safe_result[1], 2))


# Show one sample path
_, _, path = simulate("safe")
print("\nSample Safe Path:")
print(path)
