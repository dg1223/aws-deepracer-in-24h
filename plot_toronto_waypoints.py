# Python 2.7
# Shamir Alavi

import matplotlib.pyplot as plt
import numpy as np

track_name = "Canada_Training"
absolute_path = "."
waypoints = np.load("%s/%s.npy" % (absolute_path, track_name))

print("Number of waypoints = " + str(waypoints.shape[0]))

num_waypoints = 0
x = []
y = []

# plot the track
for i, point in enumerate(waypoints):
    num_waypoints += 1
    waypoint = (point[2], point[3])
    x.append(point[2])
    y.append(point[3])
    plt.scatter(waypoint[0], waypoint[1])
    plt.title('Toronto turnpike')
    # print("Waypoint " + str(i) + ": " + str(waypoint))

# initialize labels for each waypoint
label = np.arange(1,num_waypoints)

# annotate the waypoints with the labels
for i, txt in enumerate(label):
    plt.annotate(txt, (x[i], y[i]))

plt.show()
