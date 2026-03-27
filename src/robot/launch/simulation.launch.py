import os

from launch import LaunchDescription
from launch.actions import ExecuteProcess, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    package_name = 'robot'

    default_world = os.path.join(
        get_package_share_directory(package_name),
        'worlds',
        'world.sdf'
    )

    world_arg = DeclareLaunchArgument(
        'world',
        default_value=default_world,
        description='Path to world file'
    )

    world = LaunchConfiguration('world')

    urdf_file = os.path.join(
        get_package_share_directory(package_name),
        'urdf',
        'rover.urdf'
    )

    with open(urdf_file, 'r') as infp:
        robot_description = infp.read()

    rsp_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}],
        output='screen'
    )

    gazebo = ExecuteProcess(
        cmd=['gz', 'sim', '-r', world],
        output='screen'
    )

    return LaunchDescription([
        world_arg,   
        gazebo,
        rsp_node
    ])