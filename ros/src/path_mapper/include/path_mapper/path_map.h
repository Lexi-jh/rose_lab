#ifndef PATH_MAPPER__PATH_MAP_H_
#define PATH_MAPPER__PATH_MAP_H_

#include <fields2cover.h>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"



// Class responsible for publishing heartbeat messages for the path mapper node.
class PathMapper : public rclcpp::Node {
public:
  PathMapper();
  F2CLinearRing create_bounds(float corner);
  
  F2CRobot robot {2.0, 6.0};

private:
  void publish_heartbeat();

  F2CLinearRing bounds_;
  float lidar_width_{1.0F};
  float operational_width_{1.0F};
  F2CRobot robot_{lidar_width_, operational_width_};
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
  rclcpp::TimerBase::SharedPtr timer_;
};


#endif  // PATH_MAPPER__PATH_MAP_H_
