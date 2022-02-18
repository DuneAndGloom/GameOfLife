# GameOfLife
Code which I use via the terminal to visualise Conway's Game of Life, estimating the number of active or "live" cells at each timestep
Inputs at call: 
Size of grid = 50
Number of steps = 1000 (500 is usually enough to reach a steady state)
Animate? = (Y, y, N, n) -> whether or not to animate the code in matplotlib
Oscillator? = (Y, y, N, n) -> if Y/y, produces a GoL grid with only a single, randomly placed "blinker"
Glider? = (Y, y, N, n) -> if Y/y, produces a GoL grid with only a single, randomly placed "glider" which moves diagonally
