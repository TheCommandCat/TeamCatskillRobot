import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Generate data for the graph
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
y = np.array([7294,6611,6228,6024,6012,6288,6698,7153,7305,7252,7117,7018,7016,7108,7305,7653,8140,8990,9748,9922,9764,9441,8870,8220])

# Generate keyframes for the animation
num_frames = 150
keyframes = np.zeros((num_frames, len(x)))
for i in range(num_frames):
    keyframes[i,:] = y * (1 - i/num_frames) + 7500 * (i/num_frames)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 23)
ax.set_ylim(5500, max(y)+50)
ax.set_xlabel("hours of the day")
ax.set_ylabel("MWh")
ax.set_title("demonstration of our solutionh")
line, = ax.plot(x, y, label="with our solution", color="blue", linestyle="-")
ax.fill_between(x, y, label="without our solution", where=(y > 0), color="lightblue")
ax.legend()

# Define the update function for the animation
def update(num, x, keyframes, line):
    line.set_data(x, keyframes[num,:])
    ax.fill_between(x, keyframes[num,:], 7500, where=(keyframes[num,:] > 7500), color="lightblue")
    return line,

# Create the animation using the FuncAnimation function
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, num_frames), 
                              fargs=[x, keyframes, line], interval=20, blit=True)

plt.show()
