Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
======================================================= RESTART: C:/Users/hasin/AppData/Local/Programs/Python/Python314/EXP 1.py =======================================================

--- Random Policy Simulation ---
Start: (0, 0)
Step 1: (0, 0) -> LEFT -> (0, 0) | Reward: 0.0
Step 2: (0, 0) -> LEFT -> (0, 0) | Reward: 0.0
Step 3: (0, 0) -> LEFT -> (0, 0) | Reward: 0.0
Step 4: (0, 0) -> DOWN -> (1, 0) | Reward: 0.0
Step 5: (1, 0) -> RIGHT -> (1, 1) | Reward: 0.0
Step 6: (1, 1) -> RIGHT -> (1, 2) | Reward: 1.0
Step 7: (1, 2) -> RIGHT -> (1, 3) | Reward: 0.0
Step 8: (1, 3) -> RIGHT -> (1, 4) | Reward: 0.0
Step 9: (1, 4) -> UP -> (0, 4) | Reward: 0.0
Step 10: (0, 4) -> DOWN -> (1, 4) | Reward: 0.0
Step 11: (1, 4) -> LEFT -> (1, 3) | Reward: 0.0
Step 12: (1, 3) -> RIGHT -> (1, 4) | Reward: 0.0
Step 13: (1, 4) -> DOWN -> (2, 4) | Reward: 0.0
Step 14: (2, 4) -> RIGHT -> (2, 4) | Reward: 0.0
Step 15: (2, 4) -> RIGHT -> (2, 4) | Reward: 0.0
Step 16: (2, 4) -> DOWN -> (3, 4) | Reward: 0.0
Step 17: (3, 4) -> DOWN -> (4, 4) | Reward: 0.0
Step 18: (4, 4) -> RIGHT -> (4, 4) | Reward: 0.0
Step 19: (4, 4) -> RIGHT -> (4, 4) | Reward: 0.0
Step 20: (4, 4) -> UP -> (3, 4) | Reward: 0.0
Total Reward: 1.0

--- Greedy Policy Simulation ---
Start: (0, 0)
Step 1: (0, 0) -> DOWN -> (1, 0) | Reward: 0.0
Step 2: (1, 0) -> RIGHT -> (1, 1) | Reward: 0.0
Step 3: (1, 1) -> RIGHT -> (1, 2) | Reward: 1.0
Step 4: (1, 2) -> LEFT -> (1, 1) | Reward: 0.0
Step 5: (1, 1) -> RIGHT -> (1, 2) | Reward: 1.0
Step 6: (1, 2) -> LEFT -> (1, 1) | Reward: 0.0
Step 7: (1, 1) -> RIGHT -> (1, 2) | Reward: 1.0
Step 8: (1, 2) -> DOWN -> (2, 2) | Reward: -1.0
Step 9: (2, 2) -> UP -> (1, 2) | Reward: 1.0
Step 10: (1, 2) -> RIGHT -> (1, 3) | Reward: 0.0
Step 11: (1, 3) -> LEFT -> (1, 2) | Reward: 1.0
Step 12: (1, 2) -> RIGHT -> (1, 3) | Reward: 0.0
Step 13: (1, 3) -> LEFT -> (1, 2) | Reward: 1.0
Step 14: (1, 2) -> UP -> (0, 2) | Reward: 0.0
Step 15: (0, 2) -> DOWN -> (1, 2) | Reward: 1.0
Step 16: (1, 2) -> RIGHT -> (1, 3) | Reward: 0.0
Step 17: (1, 3) -> LEFT -> (1, 2) | Reward: 1.0
Step 18: (1, 2) -> DOWN -> (2, 2) | Reward: -1.0
Step 19: (2, 2) -> UP -> (1, 2) | Reward: 1.0
Step 20: (1, 2) -> UP -> (0, 2) | Reward: 0.0
Total Reward: 7.0
