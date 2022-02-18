''' Want to make an algorithm that changes the state of lattice point [i,j] between 0 (dead) and 1 (alive)
based on the states of the 8 neighbours of that cell
([i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]).
Rules:
1) If a live cell has less than 2 or more than 3 live neighbours, it will die in the next time step.
2) If a live cell has exactly 2 or 3 live neighbours, it will remain alive in the next time step.
3) A dead cell with exactly 3 live neighbours will become alive in the next time step.
'''

import matplotlib
matplotlib.use('TKAgg')

import sys
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = int(input('What is the size of grid you would like to simulate? '))
nstep = int(input('How many steps would you like to run? '))

answer = ""
while answer not in ["Y", "y", "N", "n"]:
    answer = input("Animate? (Y/N):") # asks again if not given an accepted answer

if answer in ["Y", "y"]:
    Plotting = True # Boolean True/False to either animate or not
else:
    Plotting = False

# Set initial conditions which produce a blinker (or glider, separately)

osc_answer = ""
while osc_answer not in ["Y", "y", "N", "n"]:
    osc_answer = input("Oscillator? (Y/N):")  # asks again if not given an accepted answer

if osc_answer in ["N", "n"]:
    Plotting_oscillator = False
else:
    Plotting_oscillator = True

# glider condition

glider_answer = ""
while glider_answer not in ["Y", "y", "N", "n"]:
    glider_answer = input("Glider? (Y/N):")  # asks again if not given an accepted answer

if glider_answer in ["N", "n"]:
    Plotting_glider = False
else:
    Plotting_glider = True



lx=N
ly=lx

state=np.zeros((lx,ly),dtype=float) # state is the numpy array holding all states
state_new=np.zeros((lx,ly),dtype=float)
#initialise states randomly

for i in range(lx):
    for j in range(ly):
        r=random.random()
        if(r<0.5): state[i,j]=0  # row i and col j
        if(r>=0.5): state[i,j]=1

if Plotting:
    fig = plt.figure()
    im=plt.imshow(state, animated=True)

if Plotting_oscillator:
    state = np.zeros((lx, ly), dtype=float)
    i = int(random.random()*lx)
    j = int(random.random()*ly)
    state[i, j] = 1
    state[i, j + 1] = 1
    state[i, j + 2] = 1 # makes a blinker

if Plotting_glider:
    state = np.zeros((lx, ly), dtype=float)
    i = int(random.random() * lx)
    j = int(random.random() * ly) # gives a random starting position
    state[i, j] = 1 # the top cell in a glider which goes north-east (if ly starts at 0 at the top)
    state[i-1, j+1] = 1
    state[i-2, j-1] = 1
    state[i-2, j] = 1
    state[i-2, j+1] = 1 # makes a glider which goes north-east


# implement the 3 rules:
# First, define the sum of neighbour states (= no. of live nbrs)


n_live_cells = []
n_live_cells.append(np.sum(state)) # initial conditions

for n in range(nstep):
    for i in range(lx):
        for j in range(ly):

            n_live_nbrs = (state[i - 1, j - 1] + state[i - 1, j] + state[i - 1, (j + 1) % ly] + state[i, j - 1] +
                                 state[i, (j + 1) % ly] + state[(i + 1) % lx, j - 1] + state[(i + 1) % lx, j] +
                                 state[(i + 1) % lx, (j + 1) % ly])

            if n_live_nbrs < 2 or n_live_nbrs > 3:
                state_new[i, j] = 0  # i.e. under/overcrowding, living cells die

            if (n_live_nbrs == 2 or n_live_nbrs == 3) and state[i,j] == 1:
                state_new[i, j] = 1  # i.e. stability, living cells remain alive

            if n_live_nbrs == 3 and state[i, j] == 0:
                state_new[i, j] = 1  # i.e. replication, dead cell becomes alive


    # copy the data from state_new into state, and make a new state_new

    state = np.copy(state_new) # makes a new state array containing a copy of state_new
    state_new = np.zeros((lx,ly),dtype=float)

    n_live_cells.append(np.sum(state)) # measures and updates the no. of live cells in the new state for each n

    if (n % 1 == 0):  # i.e. when the number of timesteps passes 10

        #       dump output
        f = open('GoL_data.dat', 'w')
        for i in range(lx):
            for j in range(ly):
                f.write('%d %d %lf\n' % (i, j, state[i, j]))
        f.close()

        if Plotting:
            im.set_data(state)  # update the state data with the new values
            plt.draw()
            plt.pause(0.0001)

plt.figure() # makes a new, separate figure
plt.plot(n_live_cells, 'b-')
plt.xlabel('Timestep number')
plt.ylabel('Number of live cells')
plt.show()

