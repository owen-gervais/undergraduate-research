
## Installing Ubuntu Server:

After plugging in your microSD card, type the below bash command to see the list of disks on your machine
```bash
diskutil list
```

In my case, the removable storage is on **/dev/disk2/**. Using the removable storage as your path, 
```bash
sudo diskutil eraseDisk FAT32 MYSD MBRFormat /dev/disk2
```


**Follow these steps to run:**
1. Download the supplied the robot.sdf, this model has the gazebo_ros diff_drive plugin already formatted so you should be able to control this demo by publishing to its active topics. 
2. Open two terminal windows and source the ros2/foxy installation in each as described above
3. **cd** to the folder where the robot.sdf was downloaded in both terminals
3. In the first terminal window, start the gazebo environment by running this bash command,
```bash
gazebo --verbose -s libgazebo_ros_factory.so
```
4. Once your gazebo environment is up and running, open the second terminal window and spawn the robot.sdf in your environment using this ros command
```bash
ros2 run gazebo_ros spawn_entity.py -entity diff_SPIKE -file robot.sdf
```
5. Once your robot has been spawned into the environment you can check to see the active topics being published by issuing the command
```bash
ros2 topic list
```
6. You will be able control this robot by publishing to the /cmd_demo topic using the Twist msg. Here is a sample command to send in your second terminal.
```bash
ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{angular: {z: 6.0}}' -1
```
If everything is running correctly you should see the robot rotating around the z axis quite fast!

