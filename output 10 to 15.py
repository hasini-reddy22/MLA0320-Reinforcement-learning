Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

=== RESTART: C:/Users/hasin/AppData/Local/Programs/Python/Python314/EXP 10.py ==
Episode 1000, Theta: 0.4342
Episode 2000, Theta: 0.7094
Episode 3000, Theta: 0.121
Episode 4000, Theta: 0.0345
Episode 5000, Theta: 0.5855

Final Policy:
Probability of Investing: 0.6423

=== RESTART: C:/Users/hasin/AppData/Local/Programs/Python/Python314/EXP 11.py ==
Optimal Policy (0=NS green, 1=EW green):

0 1 1 1 1 1
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

Sample State Values:
(0, 0) -> 0.0
(2, 2) -> -5.61
(5, 5) -> -34.87

=== RESTART: C:/Users/hasin/AppData/Local/Programs/Python/Python314/EXP 12.py ==
Episode: 1000
Episode: 2000
Episode: 3000
Episode: 4000
Episode: 5000

Optimal Policy (Drone Directions):

D D D D L
R R R D D
R R R D D
D U R R D
R R U R G

=== RESTART: C:/Users/hasin/AppData/Local/Programs/Python/Python314/EXP 13.py ==
State-Value Function after TD(0):

['-25.12', '-48.96', '-26.56', '-45.09', ' -0.10']
['-48.29', '  0.00', '-42.50', '  0.00', ' -0.19']
['-23.66', '-43.11', ' -0.96', ' -0.10', ' -0.10']
['-42.05', '  0.00', '  0.00', '  0.34', '  8.89']
[' -0.19', ' -5.09', '  0.00', '  0.00', '  0.00']

Derived Policy (Directions to Move):

['U', 'D', 'U', 'D', 'U']
['R', 'T', 'L', 'T', 'L']
['L', 'U', 'D', 'D', 'D']
['R', 'T', 'R', 'R', 'R']
['D', 'U', 'U', 'T', 'G']
>>> 
=== RESTART: C:/Users/hasin/AppData/Local/Programs/Python/Python314/EXP 14.py ==

Optimal Cleaning Policy:

['D', 'L', 'L', 'O', 'D']
['D', 'O', 'U', 'O', 'U']
['D', 'R', 'U', 'L', 'L']
['O', 'U', 'O', 'U', 'L']
['R', 'R', 'L', 'O', 'U']
>>> 
=== RESTART: C:/Users/hasin/AppData/Local/Programs/Python/Python314/EXP 15.py ==
Optimal Policy (Directions to Move):

['A', 'R', 'D', 'F', 'L']
['D', 'G', 'U', 'L', 'L']
['R', 'R', 'L', 'G', 'D']
['R', 'R', 'F', 'D', 'L']
['D', 'R', 'U', 'D', 'F']

Test Run Path: [(0, 0), (0, 1), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2), (1, 2), (0, 2)]
Total Reward Collected: -50
