# Dayana Gonzalez Cruz
# CST-307: Principles of Modeling 
# WF1100A Dr. Citro
# Butterfly Effect and Code Errors: Project 7: Part 2: Queue.py
# 12/10/2023

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# Purpose 1
# The purpose of this program is to display customer arrival time as a function of (1) service start time, (2) exit time, (3) time in queue, (4) number of customers in a system, and (5) number of customers in a queue

# Define lists with pre-calculated values for the system across the interval [0,15.27]

# Can intialize with numpy as finite customer pool arives at uniform intervals of 1
arrival_times = np.arange(0,15,1)

service_start_times = [0,3.22,4.98,7.11,7.25,8.1,8.8,9.27,9.49,10,12.41,12.82,13.28,14.65,15]

# a.k.a. Service End Times
exit_times = [3.22,4.98,7.11,7.25,8.1,8.8,9.27,9.49,9.67,12.41,12.82,13.28,14.65,14.92,15.27]

queue_times = [0,1.22,1.98,3.11,2.25,2.1,1.8,1.27,0.49,0,1.41,0.82,0.28,0.65,0]

# Number of customers in system at arrival of customer
num_cust_system = [0,1,2,2,2,3,4,3,2,0,1,2,1,1,0]

# Number of customers in a queue at arrival of customer
num_cust_queue = [0,0,1,1,1,2,3,2,1,0,0,1,0,0,0]

# Construct the plots 
# (1)
plt.figure(1,figsize=(15, 10))
# Plot data sets with service start time on the x 
plt.subplot(3,2,1)
plt.step(arrival_times,service_start_times, where = 'post', color = 'pink')
plt.xlabel('Customer Arrival Time (min)')
plt.ylabel('Customer Service Start Time (min)')
plt.title('Customer Arrival Time vs Service Start Time')

# (2)
plt.subplot(3,2,2)
plt.step(arrival_times, exit_times, where = 'post', color = '#97C4FF')
plt.xlabel('Customer Arrival Time (min)')
plt.ylabel('Customer Exit Time (min)')
plt.title('Customer Arrival Time vs Exit Time')

# (3)
plt.subplot(3,2,3)
plt.step(arrival_times, queue_times ,where = 'post', color = '#A2F7DB')
plt.xlabel('Customer Arrival Time (min)')
plt.ylabel('Time Spent in Queue (min)')
plt.title('Customer Arrival Time vs Time Spent in Queue')

# (4)
plt.subplot(3,2,4)
plt.step( arrival_times,num_cust_system, where = 'post', color = '#F3D9B8')
plt.xlabel('Customer Arrival Time (min)')
plt.ylabel('Number of Customers in System at Arrival')
plt.title('Customer Arrival Time vs Time Spent in Queue')

# (5)
plt.subplot(3,2,5)
plt.step(arrival_times, num_cust_queue, where = 'post', color = '#FF5096')
plt.xlabel('Customer Arrival Time (min)')
plt.ylabel('Number of Customers in Queue at Arrival')

plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.show()

# Purpose 2
# The second purpose is to model how increasing the arrival time and service rate by a factor of k in a M/M/1 system with the characteristic that arrival time is less than service rate affects the utilization, throughput, mean number of customers in the system, and mean time in the system. 

# Define arbitrary intial values for arrival time x, service rate u, and a set of increasing k values
ks = [1, 5, 10,20,50]
# Because it is given that x < u 
x = 1
u = 2

# Arrays to hold calculations
ps = np.empty_like(ks)
Xs = np.empty_like(ks)
ENs = np. empty_like(ks)
ETs = np.empty_like(ks)

# Define each equation as a function
# a.
def util(x,u):
	return x/u
# b.
def throughput(x):
	return x
# c.
def SysTime(x,u):
	p = util(x,u)
	return p/(1-p)
# d.
def QueueTime(x,u):
	p = util(x,u)
	return (1/u)/(1-p)

# Calculate for increasing ks and store
for i in range(len(ks)):
	inc_x = ks[i] * x
	inc_u = ks[i] * u	
	p = util(inc_x, inc_u)
	X = throughput(inc_x)
	EN = SysTime(inc_x,inc_u)
	ET = QueueTime(inc_x,inc_u)
	ps[i] = p
	Xs[i] = X
	ENs[i] = EN
	ETs[i] = ET
# Plot and Display
#a.
plt.figure(2,figsize=(15, 10))
plt.subplot(3,2,1)
plt.plot(ks,ps, marker = 'o', color = '#97C4FF' )
plt.title('Effect on Utilization p')
# b.
plt.subplot(3,2,2)
plt.title('Effect on Throughput X')
plt.plot(ks,Xs, marker = 'o', color ='#A2F7DB')
# c.
plt.subplot(3,2,3)
plt.xlabel('k')
plt.ylabel('E(N)')
plt.title('Effect on Mean Number of Customers in System, E(N)')
plt.plot(ks,ENs, marker = 'o', color = 'pink')
# d.
plt.subplot(3,2,4)
plt.xlabel('k')
plt.ylabel('E(T)')
plt.title('Effect on Mean Time in System, E(T)')
plt.plot(ks, ETs, marker = 'o', color = 'blue')


plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.show()
	
