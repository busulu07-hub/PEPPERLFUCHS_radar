# canopen_ws (ROS 2 Humble)

# CAN interface bring-up
Plug everything in   
Check that “lsusb | grep -i ixxat” returns something like “Bus 001 Device 008: ID 08d8:0008 IXXAT Automation GmbH USB-to-CAN V2”  
“sudo apt update”  
“sudo apt install -y build-essential dkms git”  
“mkdir -p ~/drivers/ixxat”  
Download “SocketCAN Driver for Linux” under “Linux drivers” from here https://www.hms-networks.com/support/general-downloads  
Move the file into ~/drivers/ixxat  
tar -xvf socketcan-linux  
tar -xzf ix_usb_can_2.0.520-REL.tgz  
rm -f ix_active_can_*.tgz ix_passive_can_*.tgz ix_passive_canfd_*.tgz IX_SECUREBOOT_*.tgz IX_SocketCAN-example_*.tgz socketcan-linux  
In ~/drivers/ixxat do  
make all  
sudo make install  
sudo modprobe ix_usb_can  
Now check that “ip link show” returns something like “8: can0: <NOARP,ECHO> mtu 16 qdisc noop state DOWN mode DEFAULT group default qlen 10 link/can 48:57:36:34:38:33:37:37:00:00:00:00:00:00:00:00 brd 00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00”  
sudo ip link set can0 down  
sudo ip link set can0 type can bitrate 250000  
sudo ip link set can0 up  
cansend can0 000#0100 (to put the radar into operational mode, start *all* nodes )  
candump -cae can0 (verified raw CAN communication)  


git clone https://github.com/busulu07-hub/PEPPERLFUCHS_radar.git  
cd PEPPERLFUCHS_radar  
vcs import src < canopen_ws.repos  
source /opt/ros/$ROS_DISTRO/setup.bash  
colcon build --symlink-install  

#In one terminal in /canopen_ws  
source install/setup.bash  
sudo bash -lc 'source /opt/ros/humble/setup.bash; \
               source /home/sncf/canopen_ws/install/setup.bash; \
               ROS_LOG_LEVEL=DEBUG ros2 launch canopen_config pfr.launch.py'  
Then run again with only ros2 launch canopen_config pfr.launch.py  
#In another terminal  
ros2 service call /pepperl/proxy_device_1/nmt_start_node std_srvs/srv/Trigger {}  
ros2 topic echo /pepperl/proxy_device_1/rpdo  


