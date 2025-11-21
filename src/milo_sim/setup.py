from setuptools import setup
import os
from glob import glob

package_name = 'milo_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('milo_sim/launch/*.py')),
        (os.path.join('share', package_name), glob('*.urdf')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.world')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aleja',
    maintainer_email='aleja@todo.todo',
    description='Simulación de robot Milo en Gazebo',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'odom_broadcaster = milo_sim.odom_broadcaster:main',
        ],
    },
)

