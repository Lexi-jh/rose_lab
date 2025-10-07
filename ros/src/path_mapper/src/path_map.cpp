#include "path_mapper/path_map.h"

#include <chrono>

#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

PathMapper::PathMapper() : rclcpp::Node("path_mapper_node") {
  publisher_ = this->create_publisher<std_msgs::msg::String>("path_mapper/heartbeat", 10);
  timer_ = this->create_wall_timer(1s, [this]() { publish_heartbeat(); });
}

void PathMapper::publish_heartbeat() {
  std_msgs::msg::String message;
  message.data = "path_mapper active";
  publisher_->publish(message);
  RCLCPP_DEBUG(this->get_logger(), "Published heartbeat: %s", message.data.c_str());
}
