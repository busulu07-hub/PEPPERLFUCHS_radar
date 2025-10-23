cmake_minimum_required(VERSION 3.5.0)
project(pf_radar_adapter)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_lifecycle REQUIRED)
find_package(pf_radar_interfaces_sd REQUIRED)
find_package(canopen_interfaces REQUIRED)

include_directories(
	# assure that generated .h files are found
	${PROJECT_SOURCE_DIR}/src
	${PROJECT_SOURCE_DIR}/src-gen
)

add_executable(pf_radar_adapter
	src-gen/pf_radar_adapter_cd/pf_radar_adapter.cpp
	src-gen/pf_radar_adapter_cd/pf_radar_adapter_main.cpp
	src/pf_radar_adapter_cd/pf_radar_adapter_impl.cpp
)
ament_target_dependencies(pf_radar_adapter
	rclcpp
	rclcpp_lifecycle
	pf_radar_interfaces_sd
	canopen_interfaces
)


# Start of user code dependencies
# End of user code

install(TARGETS
	pf_radar_adapter
	DESTINATION lib/${PROJECT_NAME}
)
ament_package()
