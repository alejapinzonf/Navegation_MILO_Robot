# Naviga­tion_MILO_Robot

Simulación, teleoperación y mapeo del robot **MILO** utilizando **ROS 2 Jazzy** y **Gazebo Sim 9**.

Este workspace contiene el paquete `milo_sim` con el URDF del robot, el archivo launch de Gazebo y los elementos necesarios para generar mapas 2D usando **SLAM Toolbox**.

---

## Requisitos

- ROS 2 Humble
- Gazebo Sim 9
- `robot_state_publisher`
- `gazebo_ros`
- `slam_toolbox`
- `teleop_twist_keyboard`

---

## Compilación del Workspace

```bash
colcon build
source install/setup.bash
# Si usas Zsh:
# source install/setup.zsh
```

---

## Ejecución del Sistema

### Terminal 1: Lanzar Gazebo con MILO
```bash
ros2 launch milo_sim display_gazebo.launch.py
```

### Terminal 2: Ejecutar SLAM Toolbox
```bash
ros2 launch slam_toolbox online_async_launch.py   use_sim_time:=true   base_frame:=base_link   odom_frame:=odom   map_frame:=map   scan_topic:=/scan   publish_map_transform:=true
```

### Terminal 3: Teleoperación
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

### Terminal 4: RViz2
```bash
rviz2
```

---

## Guardar el mapa

```bash
ros2 run nav2_map_server map_saver_cli -f milo_map
```

Esto genera:
- milo_map.pgm
- milo_map.yaml
