# 🤖 Simulated 4-Wheeled Mobile Robot with 6-DOF Arm

## 📝 Project Description

This project simulates a mobile robot featuring a 4-wheeled base and a 6-DOF robotic arm using ROS and Gazebo.

## 👥 Team Members

- **C.CHARAN**  
- **K.RAMU**  
- **K.VENKATESH**
  
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





