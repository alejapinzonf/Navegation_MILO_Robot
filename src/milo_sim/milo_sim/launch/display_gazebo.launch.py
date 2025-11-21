from launch import LaunchDescription
from launch.actions import ExecuteProcess, LogInfo, SetEnvironmentVariable
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    package_dir = get_package_share_directory('milo_sim')
    urdf_file = os.path.join(package_dir, 'MILO.urdf')
    world_file = os.path.join(package_dir, 'worlds', 'milo_labe.world')

    return LaunchDescription([
        LogInfo(msg=f'Usando mundo: {world_file}'),
        SetEnvironmentVariable(name='GAZEBO_WORLD_FILE', value=world_file),

        ExecuteProcess(
            cmd=['gazebo', '--verbose', world_file, '-s', 'libgazebo_ros_init.so',  '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}]
        ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-topic', 'robot_description', '-entity', 'milo'],
            output='screen'
        ),
    ])

