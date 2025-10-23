cmake_minimum_required(VERSION 3.5.0)
project(pf_radar_interfaces_sd)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(std_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)

# Start of user code dependencies
# End of user code

find_package(rosidl_default_generators REQUIRED)

# Generate messages, services or actions
rosidl_generate_interfaces(
	pf_radar_interfaces_sd
	"msg/Radar.msg"
	DEPENDENCIES std_msgs builtin_interfaces
)

ament_package()
