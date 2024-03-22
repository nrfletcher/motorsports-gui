import matplotlib.pyplot as plt
# import numpy as np

# Initialize empty plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots(8, 8)

# Main loop for updating the plot
while True:
    
    for i in range(8):
        for j in range(8):
            # Adjust plot limits if necessary
            ax[i, j].relim()
            ax[i, j].autoscale_view()

    # Draw the updated plot
    fig.canvas.draw()
    fig.canvas.flush_events()
    
    # Optional: Pause to control the refresh rate
    plt.pause(0.1)  # Adjust as needed
