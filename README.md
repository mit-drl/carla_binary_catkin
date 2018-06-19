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

Running the unittests and viewing the results can be done using the following commands

```shell
catkin build carla_binary_catkin --catkin-make-args run_tests
catkin_test_results /path/to/carla_ws/build/carla_binary_catkin/test_results/
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

## Next Steps 

If you are interested in running the CARLA server using a configuation (.ini) file, or in connecting to the server using a Python client, you can find the contents of the extracted CARLA binary at the following location in your catkin workspace:

```shell
/path/to/carla_ws/build/carla_binary_catkin/carla_binary_catkin-prefix/src/carla_binary_catkin
```

More information on how to use the configuration files and Python client files can be found in the [CARLA documentation][doclink].

[doclink]: https://carla.readthedocs.io/en/latest/
