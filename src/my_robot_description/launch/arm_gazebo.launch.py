import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'model', default_value='$(find your_package_name)/urdf/arm_gazebo.xacro',
            description='Path to the robot description file'
        ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_robot',
            output='screen',
            arguments=['-entity', 'robot', '-file', '$(arg model)']
        ),
    ])
