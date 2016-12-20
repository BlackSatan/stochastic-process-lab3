# T=10
# intens=0.587
# t=0;
# i=1;
# X=0;
# Y=0;
# while t<T
#     x=rand(1);
#     dt=-1/intens*log(x)
#     t=t+dt
#     X(i)=t;
#     Y(i)=dt;
#     i=1+i;
# end
# Z=1:(i-1)
# hist(Y)
# figure;hist(X)
# figure;bar(Z,X)
# X
# Y
import random
import math
import matplotlib.pyplot as plt
import numpy as np

T = 10
intens = 0.587
t = 0
X = []
Y = []
while t < T:
    x = random.random()
    dt = - 1 / intens * math.log(x)
    t += dt
    X.append(x)
    Y.append(dt)

fig, (ax, ax2) = plt.subplots(2)
ax.bar(np.arange(len(X)), X)
ax2.bar(np.arange(len(Y)), Y)
plt.show()
