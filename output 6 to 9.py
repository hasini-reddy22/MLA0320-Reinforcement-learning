Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
=== RESTART: C:/Users/hasin/AppData/Local/Programs/Python/Python314/EXP 6.py ===
Final Click-Through Rates (CTR):
Epsilon-Greedy: 0.1099
UCB: 0.096
Thompson Sampling: 0.1124
>>> 
=== RESTART: C:/Users/hasin/AppData/Local/Programs/Python/Python314/EXP 7.py ===

Value Function (Random Policy)
  -1.2    3.2   14.6   41.2   50.0 
  -1.6    2.0   10.3   25.3   46.0 
  -1.8    1.3    8.2   19.2   31.0 
  -1.6    2.0   10.3   25.3   46.0 
  -1.2    3.2   14.6   41.2   50.0 

Value Function (Greedy Policy)
  66.5   75.0   84.5   95.0   50.0 
  58.9   66.5   75.0   84.5   95.0 
  52.0   58.9   66.5   75.0   84.5 
  58.9   66.5   75.0   84.5   95.0 
  66.5   75.0   84.5   95.0   50.0 
>>> 
=== RESTART: C:/Users/hasin/AppData/Local/Programs/Python/Python314/EXP 8.py ===
Naive Policy -> Avg Reward: 90.0 Avg Steps: 10.0
Safe Policy  -> Avg Reward: 90.0 Avg Steps: 10.0

Sample Safe Path:
[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]
>>> 
=== RESTART: C:/Users/hasin/AppData/Local/Programs/Python/Python314/EXP 9.py ===
State Value Function (Queue Size = 0 to 5)

Random Policy:    [9.22, 12.79, 18.28, 20.29, 23.41, 27.09]
Fast-First Policy: [8.11, 22.15, 34.37, 39.69, 42.7, 43.52]
Balanced Policy:  [11.65, 11.44, 13.69, 25.14, 33.78, 38.26]
