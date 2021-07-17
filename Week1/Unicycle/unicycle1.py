"""Week I Assignment
Simulate the trajectory of a robot approximated using a unicycle model given the
following start states, dt, velocity commands and timesteps
State = (x, y, theta);
Velocity = (v, w) 
1. Start=(0, 0, 0); dt=0.1; vel=(1, 0.5); timesteps: 25
2. Start=(0, 0, 1.57); dt=0.2; vel=(0.5, 1); timesteps: 10
3. Start(0, 0, 0.77); dt=0.05; vel=(5, 4); timestep: 50
Upload the completed python file and the figures of the three sub parts in classroom
"""
import numpy as np
import matplotlib.pyplot as plt
import math

class Unicycle:
    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt

        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self, v: float, w: float, n: int):
        """
        Write the Kinematics model here
        Expectation:
            1. Given v, w and the current state self.x, self.y, self.theta
                and control commands (v, w) for n timesteps, i.e. n * dt seconds,
                return the final pose (x, y, theta) after this time.
            2. Append all intermediate points into the self.x_points, self.y_points list
                for plotting the trajectory.
        Args:
            v (float): linear velocity
            w (float): angular velocity
            n (int)  : timesteps
        Return:
            x, y, theta (float): final pose 
        """
        start = np.array([0,0,0])
        theta = start[2]
        x = 0.0
        y = 0.0

        for i in range(0, n+1):
            x = x + (v/w)*math.sin(w*0.1*i)
            y = y + (v/w) - (v/w)*math.cos(w*0.1*i)
            theta = theta + w
            self.x_points.append(round(x,3)),
            self.y_points.append(round(y,3)),
        
        print(self.x_points)
        print(self.y_points)

        return x, y, theta

    def plot(self, v: float, w: float):
        """Function that plots the intermeditate trajectory of the Robot"""
        plt.title(f"Unicycle Model: {v}, {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)
        plt.grid()

        # If you want to view the plot uncomment plt.show() and comment out plt.savefig()
        plt.show()
        # If you want to save the file, uncomment plt.savefig() and comment out plt.show()
        # plt.savefig(f"Unicycle_{v}_{w}.png")

if __name__ == "__main__":
    print("Unicycle Model Assignment")

    robotModel = Unicycle("0", "0", "0", "0.1")
    robotModel.step(1, 0.5, 25)
    robotModel.plot(1, 0.5)

    
    # make an object of the robot and plot various trajectories
# robotModel = Unicycle()
# robotModel = Unicycle("0", "0", "0", "0.1")
# robotModel.step()
# robotModel.plot()