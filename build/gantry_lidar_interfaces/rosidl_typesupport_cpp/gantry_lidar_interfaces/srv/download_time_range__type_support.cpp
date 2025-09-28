// generated from rosidl_typesupport_cpp/resource/idl__type_support.cpp.em
// with input from gantry_lidar_interfaces:srv/DownloadTimeRange.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "gantry_lidar_interfaces/srv/detail/download_time_range__functions.h"
#include "gantry_lidar_interfaces/srv/detail/download_time_range__struct.hpp"
#include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
#include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace gantry_lidar_interfaces
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _DownloadTimeRange_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _DownloadTimeRange_Request_type_support_ids_t;

static const _DownloadTimeRange_Request_type_support_ids_t _DownloadTimeRange_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _DownloadTimeRange_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _DownloadTimeRange_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _DownloadTimeRange_Request_type_support_symbol_names_t _DownloadTimeRange_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, gantry_lidar_interfaces, srv, DownloadTimeRange_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, gantry_lidar_interfaces, srv, DownloadTimeRange_Request)),
  }
};

typedef struct _DownloadTimeRange_Request_type_support_data_t
{
  void * data[2];
} _DownloadTimeRange_Request_type_support_data_t;

static _DownloadTimeRange_Request_type_support_data_t _DownloadTimeRange_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _DownloadTimeRange_Request_message_typesupport_map = {
  2,
  "gantry_lidar_interfaces",
  &_DownloadTimeRange_Request_message_typesupport_ids.typesupport_identifier[0],
  &_DownloadTimeRange_Request_message_typesupport_symbol_names.symbol_name[0],
  &_DownloadTimeRange_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t DownloadTimeRange_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_DownloadTimeRange_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
  &gantry_lidar_interfaces__srv__DownloadTimeRange_Request__get_type_hash,
  &gantry_lidar_interfaces__srv__DownloadTimeRange_Request__get_type_description,
  &gantry_lidar_interfaces__srv__DownloadTimeRange_Request__get_type_description_sources,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace gantry_lidar_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<gantry_lidar_interfaces::srv::DownloadTimeRange_Request>()
{
  return &::gantry_lidar_interfaces::srv::rosidl_typesupport_cpp::DownloadTimeRange_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, gantry_lidar_interfaces, srv, DownloadTimeRange_Request)() {
  return get_message_type_support_handle<gantry_lidar_interfaces::srv::DownloadTimeRange_Request>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "gantry_lidar_interfaces/srv/detail/download_time_range__functions.h"
// already included above
// #include "gantry_lidar_interfaces/srv/detail/download_time_range__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace gantry_lidar_interfaces
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _DownloadTimeRange_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _DownloadTimeRange_Response_type_support_ids_t;

static const _DownloadTimeRange_Response_type_support_ids_t _DownloadTimeRange_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _DownloadTimeRange_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _DownloadTimeRange_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _DownloadTimeRange_Response_type_support_symbol_names_t _DownloadTimeRange_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, gantry_lidar_interfaces, srv, DownloadTimeRange_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, gantry_lidar_interfaces, srv, DownloadTimeRange_Response)),
  }
};

typedef struct _DownloadTimeRange_Response_type_support_data_t
{
  void * data[2];
} _DownloadTimeRange_Response_type_support_data_t;

static _DownloadTimeRange_Response_type_support_data_t _DownloadTimeRange_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _DownloadTimeRange_Response_message_typesupport_map = {
  2,
  "gantry_lidar_interfaces",
  &_DownloadTimeRange_Response_message_typesupport_ids.typesupport_identifier[0],
  &_DownloadTimeRange_Response_message_typesupport_symbol_names.symbol_name[0],
  &_DownloadTimeRange_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t DownloadTimeRange_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_DownloadTimeRange_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
  &gantry_lidar_interfaces__srv__DownloadTimeRange_Response__get_type_hash,
  &gantry_lidar_interfaces__srv__DownloadTimeRange_Response__get_type_description,
  &gantry_lidar_interfaces__srv__DownloadTimeRange_Response__get_type_description_sources,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace gantry_lidar_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<gantry_lidar_interfaces::srv::DownloadTimeRange_Response>()
{
  return &::gantry_lidar_interfaces::srv::rosidl_typesupport_cpp::DownloadTimeRange_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, gantry_lidar_interfaces, srv, DownloadTimeRange_Response)() {
  return get_message_type_support_handle<gantry_lidar_interfaces::srv::DownloadTimeRange_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "gantry_lidar_interfaces/srv/detail/download_time_range__functions.h"
// already included above
// #include "gantry_lidar_interfaces/srv/detail/download_time_range__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace gantry_lidar_interfaces
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _DownloadTimeRange_Event_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _DownloadTimeRange_Event_type_support_ids_t;

static const _DownloadTimeRange_Event_type_support_ids_t _DownloadTimeRange_Event_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _DownloadTimeRange_Event_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _DownloadTimeRange_Event_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _DownloadTimeRange_Event_type_support_symbol_names_t _DownloadTimeRange_Event_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, gantry_lidar_interfaces, srv, DownloadTimeRange_Event)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, gantry_lidar_interfaces, srv, DownloadTimeRange_Event)),
  }
};

typedef struct _DownloadTimeRange_Event_type_support_data_t
{
  void * data[2];
} _DownloadTimeRange_Event_type_support_data_t;

static _DownloadTimeRange_Event_type_support_data_t _DownloadTimeRange_Event_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _DownloadTimeRange_Event_message_typesupport_map = {
  2,
  "gantry_lidar_interfaces",
  &_DownloadTimeRange_Event_message_typesupport_ids.typesupport_identifier[0],
  &_DownloadTimeRange_Event_message_typesupport_symbol_names.symbol_name[0],
  &_DownloadTimeRange_Event_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t DownloadTimeRange_Event_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_DownloadTimeRange_Event_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
  &gantry_lidar_interfaces__srv__DownloadTimeRange_Event__get_type_hash,
  &gantry_lidar_interfaces__srv__DownloadTimeRange_Event__get_type_description,
  &gantry_lidar_interfaces__srv__DownloadTimeRange_Event__get_type_description_sources,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace gantry_lidar_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<gantry_lidar_interfaces::srv::DownloadTimeRange_Event>()
{
  return &::gantry_lidar_interfaces::srv::rosidl_typesupport_cpp::DownloadTimeRange_Event_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, gantry_lidar_interfaces, srv, DownloadTimeRange_Event)() {
  return get_message_type_support_handle<gantry_lidar_interfaces::srv::DownloadTimeRange_Event>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "gantry_lidar_interfaces/srv/detail/download_time_range__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/service_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace gantry_lidar_interfaces
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _DownloadTimeRange_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _DownloadTimeRange_type_support_ids_t;

static const _DownloadTimeRange_type_support_ids_t _DownloadTimeRange_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _DownloadTimeRange_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _DownloadTimeRange_type_support_symbol_names_t;
#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _DownloadTimeRange_type_support_symbol_names_t _DownloadTimeRange_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, gantry_lidar_interfaces, srv, DownloadTimeRange)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, gantry_lidar_interfaces, srv, DownloadTimeRange)),
  }
};

typedef struct _DownloadTimeRange_type_support_data_t
{
  void * data[2];
} _DownloadTimeRange_type_support_data_t;

static _DownloadTimeRange_type_support_data_t _DownloadTimeRange_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _DownloadTimeRange_service_typesupport_map = {
  2,
  "gantry_lidar_interfaces",
  &_DownloadTimeRange_service_typesupport_ids.typesupport_identifier[0],
  &_DownloadTimeRange_service_typesupport_symbol_names.symbol_name[0],
  &_DownloadTimeRange_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t DownloadTimeRange_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_DownloadTimeRange_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
  ::rosidl_typesupport_cpp::get_message_type_support_handle<gantry_lidar_interfaces::srv::DownloadTimeRange_Request>(),
  ::rosidl_typesupport_cpp::get_message_type_support_handle<gantry_lidar_interfaces::srv::DownloadTimeRange_Response>(),
  ::rosidl_typesupport_cpp::get_message_type_support_handle<gantry_lidar_interfaces::srv::DownloadTimeRange_Event>(),
  &::rosidl_typesupport_cpp::service_create_event_message<gantry_lidar_interfaces::srv::DownloadTimeRange>,
  &::rosidl_typesupport_cpp::service_destroy_event_message<gantry_lidar_interfaces::srv::DownloadTimeRange>,
  &gantry_lidar_interfaces__srv__DownloadTimeRange__get_type_hash,
  &gantry_lidar_interfaces__srv__DownloadTimeRange__get_type_description,
  &gantry_lidar_interfaces__srv__DownloadTimeRange__get_type_description_sources,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace gantry_lidar_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<gantry_lidar_interfaces::srv::DownloadTimeRange>()
{
  return &::gantry_lidar_interfaces::srv::rosidl_typesupport_cpp::DownloadTimeRange_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_cpp, gantry_lidar_interfaces, srv, DownloadTimeRange)() {
  return ::rosidl_typesupport_cpp::get_service_type_support_handle<gantry_lidar_interfaces::srv::DownloadTimeRange>();
}

#ifdef __cplusplus
}
#endif
