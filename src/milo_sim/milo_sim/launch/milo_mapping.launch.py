from launch import LaunchDescription
from launch.actions import TimerAction
from launch_ros.actions import Node

def generate_launch_description():
    slam_node = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=[{
            'use_sim_time': True,
            'base_frame': 'base_link',
            'odom_frame': 'odom',
            'map_frame': 'map',
            'scan_topic': '/scan',
            'mode': 'mapping',
            'publish_map_transform': True
        }]
    )

    # Esperar 5 segundos para que Gazebo publique TF antes de lanzar el SLAM
    delayed_slam = TimerAction(period=5.0, actions=[slam_node])

    return LaunchDescription([delayed_slam])

