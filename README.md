# carla_binary_catkin

This repository contains a catkin package that automatically downloads and installs the (binaries of the) Carla simulator for autonomous driving research.

## Installation

If you have no catkin workspace, this package can be installed with the following commands.

```shell
source /opt/ros/kinetic/setup.bash
mkdir -p /path/to/carla_ws/src
cd /path/to/carla_ws
catkin init
cd /path/to/carla_ws/src
git clone git@github.com:mit-drl/carla_binary_catkin.git
sudo pip install -r carla_binary_catkin/requirements.txt
catkin build carla_binary_catkin
```

## Running

First make sure, that setup.bash from ros and your workspace are sourced.

```shell
source /opt/ros/kinetic/setup.bash
source /path/to/carla_ws/devel/setup.bash
```

Then, you can use rosrun to run the simulator

```shell
rosrun carla_binary_catkin CarlaUE4
```
