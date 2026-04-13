import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():

    package_name = 'robot'

    world_file = os.path.join(
        get_package_share_directory(package_name),
        'world',
        'world.sdf'
    )
   
    controller_file = os.path.join(
        get_package_share_directory(package_name), 
        'config', 
        'controller.yaml'
    )

    urdf_file = os.path.join(
    get_package_share_directory('robot'),
    'urdf',
    'rover.urdf.xacro'
     )

    robot_description = ParameterValue(
    Command(['xacro ', urdf_file]),
    value_type=str
    )

    # Robot State Publisher
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory(package_name),
                'launch',
                'rsp.launch.py'
            )
        ),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py'
            )
        ),
        launch_arguments={'gz_args': ['-r -v 4 ', world_file]}.items()
    )

    # Spawn robot (DELAYED)
    spawn_entity = TimerAction(
        period=5.0,   # wait 5 seconds
        actions=[
            Node(
                package='ros_gz_sim',
                executable='create',
                arguments=[
                    '-topic', 'robot_description',
                    '-name', 'robot',
                    '-z', '0.3'
                ],
                output='screen'
            )
        ]
    )
    controller_manager = TimerAction(
        period=6.0,
        actions=[
            Node(
                package='controller_manager',
                executable='ros2_control_node',
                parameters=[
                    {'robot_description': robot_description},
                    controller_file
                ],
                output='screen'
            )
        ]
    )

    spawn_controllers = TimerAction(
        period=8.0,
        actions=[
            Node(
                package="controller_manager",
                executable="spawner",
                arguments=["joint_state_broadcaster"],
            ),
            Node(
                package="controller_manager",
                executable="spawner",
                arguments=["diff_drive_controller"],
            ),
        ]
    )

    # Bridge
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/camera/image_raw@sensor_msgs/msg/Image@gz.msgs.Image',
            '/scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan',
            '/imu@sensor_msgs/msg/Imu@gz.msgs.IMU',
        ],
        output='screen'
    )

    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
        controller_manager,  
        spawn_controllers,
        bridge,
    ])