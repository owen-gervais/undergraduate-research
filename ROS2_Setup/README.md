# ROS2 Local Installation Steps

If you wish to set up a development enviroment on your local computer for ROS here are the steps

For this tutorial we will be using **ROS 2 Foxy** because it is the latest LTS release of ROS 2. Installation steps are taken from [here](https://index.ros.org/doc/ros2/Installation/Foxy/Linux-Install-Debians/).


## Setup Sources
```bash
sudo apt update && sudo apt install curl gnupg2 lsb-release
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

```bash
sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
```

## Install ROS 2 Packages
```bash
sudo apt update
```

If you are creating your own Ubuntu Server/Raspberry Pi image download the barebones version
```bash
sudo apt install ros-foxy-ros-base
```
Otherwise install the version with GUI tools,
```bash
sudo apt install ros-foxy-desktop
```

## Installing colcon
Colcon is the tool used to build ROS2 packages, it does not come installed in ROS so you must install standalone.
```bash
sudo apt install python3-colcon-common-extensions
```

## Creating your dev_ws
In order to build packages in ROS you must create a workspace

```bash
mkdir -p ~/dev_ws/src

cd ~/dev_ws/src

colcon build
```
You should be now able to setup and build your own packages in ROS2
