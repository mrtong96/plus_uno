### Overview ###

This is a solver for the game plus uno. This code uses A* search algorithm to solve the game.
The game can be found at:
http://marioqwe.github.io
Solutions to the first few levels can be found in sample_solutions.txt. The soltutions are a list of moves (tuples) in the form of (click this number first, click this number second).

### Usage ###

run the following command. It gives a solution to levels 2-20 in about 90 seconds:

```
$ python plus_uno_solver.py
```

### Notes ###

The search algorithm solves a simplified version of the problem in plus uno. It solves for 1 square on the board to have a value of (goal), 4 squares on the board to have values of (goal-1) and the remaining 4 to have values of (1). This allows the search algorithm to only focus on 5 tiles to solve this (4 with initial values of 1, 1 with 0). 

### Contact ###

email: mrtong96@berkeley.edu, mrtong96@gmail.com

