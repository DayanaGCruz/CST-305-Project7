# Dayana Gonzalez Cruz
# CST-307: Principles of Modeling 
# WF1100A Dr. Citro
# Program provided by instructor and adjusted 
# Butterfly Effect and Code Errors: Project 7: Part 1: Lorenz_Adjusted.py
# 12/10/2023

#-----------
#The purpose of this program is construct figures that demonstrate the change in trajectory of a Lorenz system when the initial conditions s, b, and r change. 
#---------

#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import time 
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

# Define Lorenz system
def lorenz(x, y, z, r, s, b):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot
#--------------------
# Solve for 1000 points per initial conditions change and display 1d and 3d models
def solve(r, s, b):
	# Get Start Time
	start = time.time()
	dt = 0.01 # Step size 
	num_steps = 10000

	# Need one more for the initial values
	xs = np.empty(num_steps + 1)
	ys = np.empty(num_steps + 1)
	zs = np.empty(num_steps + 1)
	
	# Set initial values 
	xs[0], ys[0], zs[0] = (5.6, 8.8, 7.4)

	# Step through "time", calculating the partial derivatives at the 	current point
	# and using them to estimate the next point
	for i in range(num_steps):
    		x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], r, s, b)
    		xs[i + 1] = xs[i] + (x_dot * dt)
    		ys[i + 1] = ys[i] + (y_dot * dt)
    		zs[i + 1] = zs[i] + (z_dot * dt)


	# Plot
	plt.figure(1)
	plt.plot(xs)
	plt.xlabel("T Axis")
	plt.ylabel("X Axis")
	plt.title("r = {}, s = {}, b = {}".format(r,s,b))
	plt.figure(2)
	plt.plot(ys)
	plt.xlabel("T Axis")
	plt.ylabel("Y Axis")
	plt.title("r = {}, s = {}, b = {}".format(r,s,b))
	plt.figure(3)
	plt.plot(zs)
	plt.xlabel("T Axis")
	plt.ylabel("Z Axis")
	plt.title("r = {}, s = {}, b = {}".format(r,s,b))
	fig = plt.figure(4)
	ax = fig.add_subplot(111, projection = '3d')
	ax = plt.gca()

	ax.plot(xs, ys, zs, lw=0.5)
	ax.set_xlabel("X Axis")
	ax.set_ylabel("Y Axis")
	ax.set_zlabel("Z Axis")
	ax.set_title("Lorenz Attractor: r = {}, s = {}, b = {}".format(r,s,b))
	# Get End Time
	end = time.time()
	# Find duration of computation and display
	ctime = end - start
	print("Computation Time: {} seconds".format(ctime)) 
	plt.show()

#--------------------
print("The purpose of this program is construct figures that demonstrate the change in trajectory of a Lorenz system when the initial conditions s, b, and r change.")
# Find solution set for various r values
again = input("Construct figure? Enter N to exit: ")
while(again != "N"):
	r = input("Give a FLOAT (ex. 0.00) for an r value:")
	s = input("Give a FLOAT (ex. 0.00) for an s value:")
	b = input("Give a FLOAT (ex. 0.00) for an b value:")
	# Cast input to floats
	r = float(r)
	s = float(s)
	b = float(b)
	solve(r,s,b)
	again = input("Construct figure? Enter N to exit: ")



