from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Get paths
    pkg_path = os.path.join(get_package_share_directory('my_robot_description'))
    urdf_path = os.path.join(pkg_path, 'urdf', 'my_robot.urdf.xacro')

    return LaunchDescription([
        # Start Gazebo
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),

        # robot_state_publisher
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            parameters=[{
                'use_sim_time': True,
                'robot_description': Command(['xacro ', urdf_path])
            }]
        ),

        # spawn_entity
        Node(
            package="gazebo_ros",
            executable="spawn_entity.py",
            arguments=[
                "-topic", "robot_description",
                "-entity", "my_robot"
            ],
            output="screen"
        ),
    ])
