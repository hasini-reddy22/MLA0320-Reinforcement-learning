import random

# Parameters
MAX_CARS = 5
GAMMA = 0.9
THETA = 1e-4

# Arrival probabilities
P_ARRIVE_NS = 0.5
P_ARRIVE_EW = 0.5

# All states
states = [(i, j) for i in range(MAX_CARS + 1)
                  for j in range(MAX_CARS + 1)]

actions = [0, 1]  # 0: NS green, 1: EW green


# Transition function
def step(state, action):
    ns, ew = state

    # Departures
    if action == 0 and ns > 0:
        ns -= 1
    elif action == 1 and ew > 0:
        ew -= 1

    # Arrivals
    if random.random() < P_ARRIVE_NS:
        ns = min(ns + 1, MAX_CARS)
    if random.random() < P_ARRIVE_EW:
        ew = min(ew + 1, MAX_CARS)

    next_state = (ns, ew)

    # Reward = negative waiting
    reward = -(ns + ew)

    return next_state, reward


# Estimate expected value (Monte Carlo approximation)
def expected_value(state, action, V, samples=10):
    total = 0
    for _ in range(samples):
        ns, ew = state
        # simulate deterministically multiple times
        ns_temp, ew_temp = ns, ew

        # Departures
        if action == 0 and ns_temp > 0:
            ns_temp -= 1
        elif action == 1 and ew_temp > 0:
            ew_temp -= 1

        # Expected arrivals (approx)
        ns_temp = min(ns_temp + int(P_ARRIVE_NS), MAX_CARS)
        ew_temp = min(ew_temp + int(P_ARRIVE_EW), MAX_CARS)

        reward = -(ns_temp + ew_temp)
        total += reward + GAMMA * V[(ns_temp, ew_temp)]

    return total / samples


# -----------------------------
# Policy Iteration
# -----------------------------
def policy_iteration():
    # Initialize
    V = {s: 0.0 for s in states}
    policy = {s: random.choice(actions) for s in states}

    while True:
        # ---------------------
        # Policy Evaluation
        # ---------------------
        while True:
            delta = 0
            new_V = V.copy()

            for s in states:
                a = policy[s]
                v = expected_value(s, a, V)
                delta = max(delta, abs(v - V[s]))
                new_V[s] = v

            V = new_V
            if delta < THETA:
                break

        # ---------------------
        # Policy Improvement
        # ---------------------
        policy_stable = True

        for s in states:
            old_action = policy[s]

            values = []
            for a in actions:
                values.append(expected_value(s, a, V))

            best_action = actions[values.index(max(values))]
            policy[s] = best_action

            if old_action != best_action:
                policy_stable = False

        if policy_stable:
            break

    return policy, V


# Run algorithm
policy, V = policy_iteration()


# -----------------------------
# Display Results
# -----------------------------
print("Optimal Policy (0=NS green, 1=EW green):\n")

for i in range(MAX_CARS + 1):
    row = []
    for j in range(MAX_CARS + 1):
        row.append(str(policy[(i, j)]))
    print(" ".join(row))

print("\nSample State Values:")
for s in [(0,0), (2,2), (5,5)]:
    print(s, "->", round(V[s], 2))
