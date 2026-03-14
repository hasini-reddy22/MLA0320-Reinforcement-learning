import numpy as np

# Grid size
GRID_SIZE = 5
gamma = 0.9

# Delivery points
delivery_points = [(4,4), (2,3)]

# Reward grid
rewards = -1 * np.ones((GRID_SIZE, GRID_SIZE))

for d in delivery_points:
    rewards[d] = 10

# Actions
actions = ["UP","DOWN","LEFT","RIGHT"]

# Initialize policy randomly
policy = np.random.choice(actions, (GRID_SIZE, GRID_SIZE))

# Value function
V = np.zeros((GRID_SIZE, GRID_SIZE))


# Movement function
def move(state, action):

    r,c = state

    if action == "UP":
        r = max(r-1,0)
    elif action == "DOWN":
        r = min(r+1, GRID_SIZE-1)
    elif action == "LEFT":
        c = max(c-1,0)
    elif action == "RIGHT":
        c = min(c+1, GRID_SIZE-1)

    return (r,c)


# ----------------------------
# Policy Evaluation
# ----------------------------
def policy_evaluation():

    theta = 0.001

    while True:

        delta = 0

        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):

                state = (r,c)
                action = policy[r,c]

                next_state = move(state, action)

                value = rewards[next_state] + gamma * V[next_state]

                delta = max(delta, abs(value - V[state]))

                V[state] = value

        if delta < theta:
            break


# ----------------------------
# Policy Improvement
# ----------------------------
def policy_improvement():

    policy_stable = True

    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):

            state = (r,c)
            old_action = policy[r,c]

            action_values = []

            for a in actions:

                next_state = move(state,a)

                action_values.append(rewards[next_state] + gamma * V[next_state])

            best_action = actions[np.argmax(action_values)]

            policy[r,c] = best_action

            if old_action != best_action:
                policy_stable = False

    return policy_stable


# ----------------------------
# Policy Iteration Loop
# ----------------------------
while True:

    policy_evaluation()

    if policy_improvement():
        break


print("Optimal Value Function:")
print(V)

print("\nOptimal Policy:")
print(policy)
