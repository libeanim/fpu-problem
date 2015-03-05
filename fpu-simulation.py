"""
===========================================
Simulation of the Fermi-Pasta-Ulam problem
===========================================

Visit "https://github.com/libeanim/fpu-problem" for further information.

:license: GPLv2
:date:    05.03.2015
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

__version__ = '1.0'

print(__doc__)
print('version:', __version__)

# FUNCTION DEFINITION

def total_energy(x, x_old, n_particles, dt):
    """total energy of the system"""
    v = (x - x_old) / dt
    dx = (x + x_old - np.roll(x, 1) - np.roll(x_old, 1)) / 2.0
    dx[0:1] = 0
    v[0:1] = 0
    return np.sum(0.5 * v**2 + 0.5 * dx**2)

def mode_energy(x, x_old, n_particles, k, dt):
    """energy of mode k"""
    tmp = np.arange(0, n_particles + 2, 1)
    tmp[-1:] = 0
    m = np.sqrt(2.0 / (n_particles + 1)) * np.dot(x, np.sin( ( tmp * k * np.pi / (n_particles + 1) ) ))
    m_old = np.sqrt(2.0 / (n_particles + 1)) * np.dot(x_old, np.sin( ( tmp * k * np.pi / (n_particles + 1) ) ))
    return 0.5 * (m - m_old)**2 / dt**2 + 0.5 * (m + m_old)**2 * np.sin( np.pi * k / (2 * (n_particles + 1)) )**2

def force(x):
    """Force on (n_particle +  2)/2"""
    p = int(x.size / 2)
    f = x[p + 1] + x[p - 1] - 2 * x[p] 
    return f


# INITIALIZING VARIABLES

## number of particles (+2 for the stationary ones at the edges)
n_particles = 32

## timestep dt
dt = 0.2

## maximal time
t_max = 20000
#t_max = 100000

## Set alpha and beta
alpha = 0
beta = 0.3

# SETTING STARTPOSTION

## change the initial mode to get different harmonics
init_mode = 1

amplitude = 10 * np.sqrt(2.0 / (n_particles + 1))
lamb = 2 / init_mode

tmp = np.arange(0, n_particles + 2, 1)

x = x_old = amplitude * np.sin(2.0 * np.pi * tmp / ( lamb * (n_particles + 1) ))
x[0:1] = x[-1:] = x_old[0:1] = x_old[-1:] = 0

pos = np.linspace(0, n_particles + 2, num=n_particles + 2)
plt.title('Start position of particles')
plt.axis([0, n_particles + 2, -amplitude * 1.1, amplitude * 1.1])
plt.plot(pos, x, 'ro')
plt.show()


# CALCULATING x, total energy and mode energy

print('Calculating...')

t = 0
data = {                                                                \
        'x':[x],                                                        \
        'total_energy':[total_energy(x, x_old, n_particles, dt)],       \
        'mode1':[mode_energy(x, x_old, n_particles, 1, dt)],            \
        'mode2':[mode_energy(x, x_old, n_particles, 2, dt)],            \
        'mode3':[mode_energy(x, x_old, n_particles, 3, dt)],            \
        'force':[force(x)]
        }
dtq = dt**2
while t < t_max:
    #calculating new position of particles
    x, x_old = (                                                                        \
                (np.roll(x, -1) + np.roll(x, 1) - 2.0 * x) * dtq                        \
                + alpha * ( (np.roll(x, -1) - x)**2 - (x - np.roll(x, 1))**2 ) * dtq    \
                + beta * ( (np.roll(x, -1) - x)**3 - (x - np.roll(x, 1))**3 ) * dtq     \
                + 2.0 * x - x_old,                                                      \
                x                                                                       \
               )
    x[0:1] = 0
    x[-1:] = 0
    
    data['x'].append(x)
    data['total_energy'].append(total_energy(x, x_old, n_particles, dt))
    data['mode1'].append(mode_energy(x, x_old, n_particles, 1, dt))
    data['mode2'].append(mode_energy(x, x_old, n_particles, 2, dt))
    data['mode3'].append(mode_energy(x, x_old, n_particles, 3, dt))
    data['force'].append(force(x))
    t += dt
data['time'] = np.linspace(0, len(data['x']), num=len(data['x'])) * dt
## convert to numpy-array:
data['total_energy'], data['mode1'], data['mode2'], data['mode3'], data['force'] = np.array(data['total_energy']), np.array(data['mode1']), np.array(data['mode2']), np.array(data['mode3']), np.array(data['force'])
print('done')


# ANIMATION
## Save as mp4 or plot live

fig = plt.figure(figsize=(10.0, 8.0), dpi=70)

print('Generating plots...')
pos = np.linspace(0, n_particles + 2, num=n_particles + 2)
im_particle = []
plt.axis([0, n_particles + 2, -amplitude * 1.1, amplitude * 1.1])
for d in data['x'][0:1000]:
    im_particle.append(plt.plot(pos, d, 'ro'))
print('done')

im_ani = animation.ArtistAnimation(fig, im_particle, interval=20, repeat_delay=3000, blit=True)

# You can now choose between a live animation or if your animation is directly saved to a mp4 file.
# Only one option is possible at the same time. So uncomment and recomment accordingly.

##  Show animation live:
### uncomment following statement and recomment those below:

plt.show()

##  End of animation

##  Save as mp4-file:
### uncomment following statements and recomment those above:

#print('Creating mp4 file...')
#im_ani.save('im_a' + str(alpha) + '_b' + str(beta) + '_str(init_mode).mp4', writer='avconv')
#plt.close()
#print('done')

##  End of mp4-file


# PLOTAREA
## plot some results
plt.figure(figsize=(10, 8))
plt.plot(data['time'], data['total_energy'], 'r')
plt.axis([0, t_max, 0, np.max(data['total_energy']) * 1.2])
plt.xlabel('Time t in a.u.')
plt.ylabel('Energy E in a.u.')
plt.title('Total energy')
plt.show()

plt.figure(figsize=(10, 8))
plt.plot(data['time'], data['mode1'], 'r', label='Mode 1')
plt.plot(data['time'], data['mode3'], 'b', label='Mode 2')
plt.xlabel('Time t in a.u.')
plt.ylabel('Energy E in a.u.')
plt.title('Mode energy')
plt.legend()
plt.show()