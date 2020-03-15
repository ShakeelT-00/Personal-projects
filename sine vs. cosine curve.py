# This program generates a sine vs. cosine curve

import numpy as np
import matplotlib.pyplot as plot

time = np.arange(-10, 10, 0.001)  # Setting the x values

# Amplitude of the sine and cosine wave is sine/cosine of a variable like time
amplitude_sin = np.sin(time)
amplitude_cos = np.cos(time)

# Plot a sine vs. cosine wave using time and amplitude obtained for the sine and cosine wave
plot.plot(time, amplitude_sin)
plot.plot(time, amplitude_cos)

# Title for the graph
plot.title('Sine vs. Cosine curve')

# x-axis label
plot.xlabel('Time')

# y-axis label
plot.ylabel('Amplitude = sin(time)')

# Grid lines
plot.grid(True, which='both')
plot.axhline(y=0, color='k')

plot.show()


# Reference: https://pythontic.com/visualization/charts/sinewave
