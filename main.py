
import random
import math
import matplotlib.pyplot as plt
import numpy as np

T = 50
intens = 0.587
t = 0
X = []
Y = []
T_LOG = []
event_num_probabilities = []
event_count = 0
#Run proccess
while t < T:
    x = random.random()
    dt = - 1 / intens * math.log(x)
    t += dt
    X.append(x)
    Y.append(dt)
    T_LOG.append(t)
    event_count += 1


for i in range(T):
    event_num_probability = ((intens * T) ** i * (math.e ** -(intens * T))) / math.factorial(i)
    event_num_probabilities.append(event_num_probability)
fig, (ax, ax2, ax3) = plt.subplots(3)
ax.bar(np.arange(len(event_num_probabilities)), event_num_probabilities, label='probability of occurrence of n events')
ax.legend(loc='upper left')
ax2.bar(np.arange(len(Y)), Y, label='Interval between evens')
ax2.legend(loc='upper left')
ax3.bar(np.arange(len(T_LOG)), T_LOG, label='time of occurrence given event')
ax3.legend(loc='upper left')
plt.show()
