# pf_radar.launch.py
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
      """Generate launch description with multiple components."""
      path_file = os.path.dirname(__file__)

      ld = LaunchDescription()


      device_container = IncludeLaunchDescription(
          PythonLaunchDescriptionSource(
              [
                  os.path.join(get_package_share_directory("canopen_core"), "launch"),
                  "/canopen.launch.py",
              ]
          ),
          launch_arguments={
              "master_config": os.path.join(
                  get_package_share_directory("canopen_config"),
                  "config",
                  "bus_config",
                  "master.dcf",
              ),
              "master_bin": os.path.join(
                  get_package_share_directory("canopen_config"),
                  "config",
                  "bus_config",
                  "master.bin",
              ),
              "bus_config": os.path.join(
                  get_package_share_directory("canopen_config"),
                  "config",
                  "bus_config",
                  "bus.yml",
              ),
              "can_interface_name": "can0",
          }.items(),

      )

      ld.add_action(device_container)

      return ld