import matplotlib.pyplot as plt
import numpy as np

# Some example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

fig, axs = plt.subplots(8, 8, figsize=(12, 7))

for i in range(8):
    for j in range(8):
        #axs[i, j].plot(x, y)
        axs[i, j].set_facecolor('xkcd:salmon')

#for ax in axs.flat:
 #   ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
#for ax in axs.flat:
 #   ax.label_outer()


plt.show()