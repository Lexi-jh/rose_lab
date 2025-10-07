cmake_minimum_required(VERSION 3.8)
project(path_mapper)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(Fields2Cover REQUIRED)

add_executable(path_mapper_node
  src/path_main.cpp
  src/path_map.cpp
)

target_include_directories(path_mapper_node
  PRIVATE
    include
)

ament_target_dependencies(path_mapper_node
  rclcpp
  std_msgs
  Fields2Cover
)

target_link_libraries(path_mapper_node
  Fields2Cover::Fields2Cover
)

install(TARGETS path_mapper_node
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY include/
  DESTINATION include
)

ament_export_include_directories(include)
ament_export_dependencies(rclcpp std_msgs Fields2Cover)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
