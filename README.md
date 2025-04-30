# 🤖 Simulated 4-Wheeled Mobile Robot with 6-DOF Arm

## 📝 Project Description

This project simulates a mobile robot featuring a 4-wheeled base and a 6-DOF robotic arm using ROS and Gazebo.

## 👥 Team Members

- **C.CHARAN**  
- **K.RAMU**  
- **K.VENKATESH**

## 💻 System Configuration

This simulation was developed and tested on the following system:

- **Operating System**: Ubuntu 22.04 LTS  
- **ROS 2 Distribution**: Humble Hawksbill  
- **Simulator**: Gazebo  
---
 
## 🛠️ Tech Stack & Tools Used

This project uses the following technologies and tools for simulating and visualizing the mobile robot with a 6-DOF arm:

- **ROS 2 (Robot Operating System)** – Middleware for robot software development
- **Gazebo** – 3D robotics simulator for testing robot behavior in virtual environments
- **RViz** – Visualization tool for robot state, TFs, and sensor data
- **URDF / Xacro** – For defining the robot's physical structure and joint configurations
- **Python** – Used in ROS 2 launch files and scripts (e.g., `arm_gazebo.launch.py`)
- **XML** – Used in older-style launch files and robot descriptions (e.g., `display.launch.xml`)
- **YAML** – Configuration files (e.g., `arm_controllers.yaml`) for controllers and plugins
- **CMake / package.xml** – Standard ROS 2 package configuration and build system

### 🗂️ Key Packages

- `my_robot_description/` – Contains URDF/Xacro files, robot structure, sensors, and configurations
- `my_robot_bringup/` – Launch files for starting the simulation, RViz, and Gazebo
- `worlds/` – Custom simulation world (e.g., `test_world.world`)
- `rviz/` – RViz visualization configuration

# Two-Wheeled Robot with Jointed Arm

## Project Overview

We started this project with a two-wheeled robot design, incorporating one caster wheel for stability. The robot is equipped with a two-jointed arm to enable basic manipulation tasks. Our goal is to create a functional robot capable of autonomous movement and object interaction. The project serves as a foundation for further exploration and enhancements in robotics.
## Usage
## 1. Launch the Robot in Gazebo
### To start the robot simulation in Gazebo, use the following launch command:
```bash
ros2 launch my_robot_bringup my_robot_gazebo.launch.xml
```
![Robot Image](images/robot2.png)

## 2. Launch the Robot Description in RViz
### To visualize the robot model in RViz, use the following command:

```bash
ros2 launch my_robot_description display.launch.py
```
![Robot Image](images/robot1.png)

## 3. Control the Movement of the 4-Wheeled Robot
### To control the robot's movement using keyboard teleoperation, run the following command:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/cmd_vel
```
## 4. Test the Arm Movement
### To test the arm's movement, publish a joint trajectory using the following command:

```bash
ros2 topic pub -1 /set_joint_trajectory trajectory_msgs/msg/JointTrajectory '{header: {frame_id: "base_footprint"}, joint_names: ["arm_base_forearm_joint", "forearm_hand_joint"], points: [{positions: [0.1, 0.4]}]}'
```





