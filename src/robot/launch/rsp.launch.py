import os
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    package_name = 'robot'

    urdf_file = os.path.join(
        get_package_share_directory(package_name),
        'urdf',
        'rover.urdf'
    )

    # Read URDF file directly
    with open(urdf_file, 'r') as infp:
        robot_description = infp.read()   
    )

    # Robot State Publisher Node
    rsp_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            'robot_description': robot_description
        }],
        output='screen'
    )

    return LaunchDescription([
        rsp_node
    ])