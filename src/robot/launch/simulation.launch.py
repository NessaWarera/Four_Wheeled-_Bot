import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import ExecuteProcess

def generate_launch_description():

    package_name = 'robot'

    # Include rsp.launch.py
    rsp_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory(package_name),
                'launch',
                'rsp.launch.py'
            )
        )
    )

    gazebo = ExecuteProcess(
    cmd=['gz', 'sim', '-r', 'world.sdf'],
    output='screen'
)

    spawn_entity = Node(
    package='ros_gz_sim',
    executable='create',
    arguments=[
        '-topic', 'robot_description',
        '-name', 'rover'
    ],
    output='screen'
)

    return LaunchDescription([
        rsp_launch,
        gazebo,
        spawn_entity
    ])