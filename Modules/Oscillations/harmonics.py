import matplotlib.pyplot as plt
import math

# Constants
fundamental_frequency = 440.0 # A = 440 Hz
fundamental_amplitude = 2.0

# Up an octave
first_frequency = fundamental_frequency * 2.0 # Hz
first_amplitude = fundamental_amplitude * 0.5

# Up a fifth more
second_frequency = fundamental_frequency * 3.0 # Hz
second_amplitude = fundamental_amplitude * 0.4

# Show 9/1000ths of a second of the waveform
max_time = 0.0092 # seconds

# Calculate the values 10,000 times per second
time_step = 0.00001 # seconds

# Initialize 
time = 0.0
times = []
totals = []
fundamentals = []
firsts = []
seconds = []

while time <= max_time:
    # Store the time
    times.append(time)
    
    # Compute value each harmonic
    fundamental = fundamental_amplitude * math.sin(2.0 * math.pi * fundamental_frequency * time)
    first = first_amplitude * math.sin(2.0 * math.pi * first_frequency * time)
    second = second_amplitude * math.sin(2.0 * math.pi * second_frequency * time)

    # Sum them up
    total = fundamental + first + second

    # Store the values
    fundamentals.append(fundamental)
    firsts.append(first)
    seconds.append(second)
    totals.append(total)

    # Increment time
    time += time_step

# Plot the data
fig, ax = plt.subplots(2, 1)

# Show each component
ax[0].plot(times, fundamentals)
ax[0].plot(times, firsts)
ax[0].plot(times, seconds)
ax[0].legend()

# Show the totals
ax[1].plot(times, totals)
ax[1].set_xlabel("Time (s)")

plt.show()

