# [Kaia.ai](https://kaia.ai) ROS2 pet robots

- 3D printable models of [Kaia.ai](https://kaia.ai) DIY pet robots [repo](https://github.com/kaiaai/3d_printables)
- Arduino ESP32 robot firmware [repo](https://github.com/kaiaai/arduino_fw/)
- Micro-ROS Arduino library for Kaia.ai robots [repo](https://github.com/kaiaai/micro_ros_arduino_kaia/)
- end-user and development ROS2 Docker images [repo](https://github.com/kaiaai/docker/)
- robot simulation ROS2 packages [repo](https://github.com/kaiaai/kaia_simulations/)
- ROS2 messages package for Kaia.ai robots [repo](https://github.com/kaiaai/kaia_msgs/)
- DIY electronic hardware, PCB designs for Kaia.ai robots [repo](https://github.com/kaiaai/electronics/)

## Command cheat sheet
Use these commands to operate the default Kaia.ai `snoopy` robot:
```
# Launch the physical robot
ros2 launch kaia_bringup main.launch.py

# Monitor robot's sensors
ros2 launch kaia_bringup rviz2.launch.py

# Launch the robot in a simulation - drive manually or let it self-drive itself
ros2 launch kaia_gazebo world.launch.py
ros2 run kaia_teleop teleop_keyboard
ros2 run kaia_gazebo kaia_self_drive
ros2 launch kaia_bringup rviz2.launch.py

# Launch the robot in a simulation - create, save a map
ros2 launch kaia_gazebo world.launch.py
ros2 launch kaia_bringup cartographer.launch.py use_sim_time:=True
ros2 run kaia_gazebo kaia_self_drive
ros2 run nav2_map_server map_saver_cli -f $HOME/my_map

# Launch the robot in a simulation - let it navigate automatically using an existing map
ros2 launch kaia_gazebo world.launch.py
ros2 launch kaia_bringup nav2.launch.py use_sim_time:=True map:=$HOME/my_map.yaml

# Inspect robot's URDF model - useful when modding a robot
ros2 launch kaia_bringup inspect_urdf.launch.py
```

## Command cheat sheet - for a modded robot
Let's assume your modded robot is called `waldo` and all its description files reside
in `waldo_description` package.
```
# Launch the physical robot
ros2 launch kaia_bringup main.launch.py description:=waldo_description

# Monitor robot's sensors
ros2 launch kaia_bringup rviz2.launch.py description:=waldo_description

# Launch the robot in a simulation - drive manually or let it self-drive itself
ros2 launch kaia_gazebo world.launch.py description:=waldo_description
ros2 run kaia_teleop teleop_keyboard description:=waldo_description
ros2 run kaia_gazebo kaia_self_drive description:=waldo_description
ros2 launch kaia_bringup rviz2.launch.py description:=waldo_description

# Launch the robot in a simulation - create, save a map
ros2 launch kaia_gazebo world.launch.py description:=waldo_description
ros2 launch kaia_bringup cartographer.launch.py use_sim_time:=True description:=waldo_description
ros2 run kaia_gazebo kaia_self_drive description:=waldo_description
ros2 run nav2_map_server map_saver_cli -f $HOME/my_map

# Launch the robot in a simulation - let it navigate automatically using an existing map
ros2 launch kaia_gazebo world.launch.py description:=waldo_description
ros2 launch kaia_bringup nav2.launch.py use_sim_time:=True map:=$HOME/my_map.yaml description:=waldo_description

# Inspect robot's URDF model - useful when modding a robot
ros2 launch kaia_bringup inspect_urdf.launch.py description:=waldo_description
```

## Acknowledgements
Initial versions of packages in this repo are based on ROBOTIS
[Turtlebot3 code](https://github.com/ROBOTIS-GIT/turtlebot3)
