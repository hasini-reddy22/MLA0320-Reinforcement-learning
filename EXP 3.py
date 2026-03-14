import numpy as np

# States: 0=Low, 1=Medium, 2=High traffic
states = 3

# Actions: 0=Short, 1=Medium, 2=Long green signal
actions = 3

gamma = 0.9

# Reward matrix R[s][a]
R = np.array([
    [5, 4, 3],    # Low traffic
    [2, 4, 3],    # Medium traffic
    [-5, 1, 4]    # High traffic
])

# Transition probabilities P[s][a][s']
P = np.array([
    [[0.7,0.3,0.0], [0.6,0.4,0.0], [0.5,0.5,0.0]],
    [[0.2,0.6,0.2], [0.3,0.5,0.2], [0.4,0.4,0.2]],
    [[0.1,0.4,0.5], [0.2,0.5,0.3], [0.3,0.5,0.2]]
])

# Initialize random policy
policy = np.random.randint(actions, size=states)

# Value function
V = np.zeros(states)

theta = 0.001


# ------------------------
# Policy Evaluation
# ------------------------
def policy_evaluation():
    global V
    while True:
        delta = 0
        for s in range(states):
            v = V[s]
            a = policy[s]

            V[s] = R[s][a] + gamma * sum(
                P[s][a][s2] * V[s2] for s2 in range(states)
            )

            delta = max(delta, abs(v - V[s]))

        if delta < theta:
            break


# ------------------------
# Policy Improvement
# ------------------------
def policy_improvement():

    policy_stable = True

    for s in range(states):

        old_action = policy[s]

        action_values = []

        for a in range(actions):

            value = R[s][a] + gamma * sum(
                P[s][a][s2] * V[s2] for s2 in range(states)
            )

            action_values.append(value)

        best_action = np.argmax(action_values)

        policy[s] = best_action

        if old_action != best_action:
            policy_stable = False

    return policy_stable


# ------------------------
# Policy Iteration Loop
# ------------------------
while True:

    policy_evaluation()

    if policy_improvement():
        break


print("Optimal Value Function:")
print(V)

print("\nOptimal Traffic Light Policy:")
print(policy)
