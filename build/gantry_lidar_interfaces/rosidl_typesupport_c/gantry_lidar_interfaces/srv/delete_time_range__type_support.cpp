// generated from rosidl_typesupport_c/resource/idl__type_support.cpp.em
// with input from gantry_lidar_interfaces:srv/DeleteTimeRange.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "gantry_lidar_interfaces/srv/detail/delete_time_range__struct.h"
#include "gantry_lidar_interfaces/srv/detail/delete_time_range__type_support.h"
#include "gantry_lidar_interfaces/srv/detail/delete_time_range__functions.h"
#include "rosidl_typesupport_c/identifier.h"
#include "rosidl_typesupport_c/message_type_support_dispatch.h"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_c/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace gantry_lidar_interfaces
{

namespace srv
{

namespace rosidl_typesupport_c
{

typedef struct _DeleteTimeRange_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _DeleteTimeRange_Request_type_support_ids_t;

static const _DeleteTimeRange_Request_type_support_ids_t _DeleteTimeRange_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _DeleteTimeRange_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _DeleteTimeRange_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _DeleteTimeRange_Request_type_support_symbol_names_t _DeleteTimeRange_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, gantry_lidar_interfaces, srv, DeleteTimeRange_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, gantry_lidar_interfaces, srv, DeleteTimeRange_Request)),
  }
};

typedef struct _DeleteTimeRange_Request_type_support_data_t
{
  void * data[2];
} _DeleteTimeRange_Request_type_support_data_t;

static _DeleteTimeRange_Request_type_support_data_t _DeleteTimeRange_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _DeleteTimeRange_Request_message_typesupport_map = {
  2,
  "gantry_lidar_interfaces",
  &_DeleteTimeRange_Request_message_typesupport_ids.typesupport_identifier[0],
  &_DeleteTimeRange_Request_message_typesupport_symbol_names.symbol_name[0],
  &_DeleteTimeRange_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t DeleteTimeRange_Request_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_DeleteTimeRange_Request_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
  &gantry_lidar_interfaces__srv__DeleteTimeRange_Request__get_type_hash,
  &gantry_lidar_interfaces__srv__DeleteTimeRange_Request__get_type_description,
  &gantry_lidar_interfaces__srv__DeleteTimeRange_Request__get_type_description_sources,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace gantry_lidar_interfaces

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, gantry_lidar_interfaces, srv, DeleteTimeRange_Request)() {
  return &::gantry_lidar_interfaces::srv::rosidl_typesupport_c::DeleteTimeRange_Request_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "gantry_lidar_interfaces/srv/detail/delete_time_range__struct.h"
// already included above
// #include "gantry_lidar_interfaces/srv/detail/delete_time_range__type_support.h"
// already included above
// #include "gantry_lidar_interfaces/srv/detail/delete_time_range__functions.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
// already included above
// #include "rosidl_typesupport_c/message_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_c/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace gantry_lidar_interfaces
{

namespace srv
{

namespace rosidl_typesupport_c
{

typedef struct _DeleteTimeRange_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _DeleteTimeRange_Response_type_support_ids_t;

static const _DeleteTimeRange_Response_type_support_ids_t _DeleteTimeRange_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _DeleteTimeRange_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _DeleteTimeRange_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _DeleteTimeRange_Response_type_support_symbol_names_t _DeleteTimeRange_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, gantry_lidar_interfaces, srv, DeleteTimeRange_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, gantry_lidar_interfaces, srv, DeleteTimeRange_Response)),
  }
};

typedef struct _DeleteTimeRange_Response_type_support_data_t
{
  void * data[2];
} _DeleteTimeRange_Response_type_support_data_t;

static _DeleteTimeRange_Response_type_support_data_t _DeleteTimeRange_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _DeleteTimeRange_Response_message_typesupport_map = {
  2,
  "gantry_lidar_interfaces",
  &_DeleteTimeRange_Response_message_typesupport_ids.typesupport_identifier[0],
  &_DeleteTimeRange_Response_message_typesupport_symbol_names.symbol_name[0],
  &_DeleteTimeRange_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t DeleteTimeRange_Response_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_DeleteTimeRange_Response_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
  &gantry_lidar_interfaces__srv__DeleteTimeRange_Response__get_type_hash,
  &gantry_lidar_interfaces__srv__DeleteTimeRange_Response__get_type_description,
  &gantry_lidar_interfaces__srv__DeleteTimeRange_Response__get_type_description_sources,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace gantry_lidar_interfaces

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, gantry_lidar_interfaces, srv, DeleteTimeRange_Response)() {
  return &::gantry_lidar_interfaces::srv::rosidl_typesupport_c::DeleteTimeRange_Response_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "gantry_lidar_interfaces/srv/detail/delete_time_range__struct.h"
// already included above
// #include "gantry_lidar_interfaces/srv/detail/delete_time_range__type_support.h"
// already included above
// #include "gantry_lidar_interfaces/srv/detail/delete_time_range__functions.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
// already included above
// #include "rosidl_typesupport_c/message_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_c/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace gantry_lidar_interfaces
{

namespace srv
{

namespace rosidl_typesupport_c
{

typedef struct _DeleteTimeRange_Event_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _DeleteTimeRange_Event_type_support_ids_t;

static const _DeleteTimeRange_Event_type_support_ids_t _DeleteTimeRange_Event_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _DeleteTimeRange_Event_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _DeleteTimeRange_Event_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _DeleteTimeRange_Event_type_support_symbol_names_t _DeleteTimeRange_Event_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, gantry_lidar_interfaces, srv, DeleteTimeRange_Event)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, gantry_lidar_interfaces, srv, DeleteTimeRange_Event)),
  }
};

typedef struct _DeleteTimeRange_Event_type_support_data_t
{
  void * data[2];
} _DeleteTimeRange_Event_type_support_data_t;

static _DeleteTimeRange_Event_type_support_data_t _DeleteTimeRange_Event_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _DeleteTimeRange_Event_message_typesupport_map = {
  2,
  "gantry_lidar_interfaces",
  &_DeleteTimeRange_Event_message_typesupport_ids.typesupport_identifier[0],
  &_DeleteTimeRange_Event_message_typesupport_symbol_names.symbol_name[0],
  &_DeleteTimeRange_Event_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t DeleteTimeRange_Event_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_DeleteTimeRange_Event_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
  &gantry_lidar_interfaces__srv__DeleteTimeRange_Event__get_type_hash,
  &gantry_lidar_interfaces__srv__DeleteTimeRange_Event__get_type_description,
  &gantry_lidar_interfaces__srv__DeleteTimeRange_Event__get_type_description_sources,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace gantry_lidar_interfaces

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, gantry_lidar_interfaces, srv, DeleteTimeRange_Event)() {
  return &::gantry_lidar_interfaces::srv::rosidl_typesupport_c::DeleteTimeRange_Event_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "gantry_lidar_interfaces/srv/detail/delete_time_range__type_support.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
#include "rosidl_typesupport_c/service_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
#include "service_msgs/msg/service_event_info.h"
#include "builtin_interfaces/msg/time.h"

namespace gantry_lidar_interfaces
{

namespace srv
{

namespace rosidl_typesupport_c
{
typedef struct _DeleteTimeRange_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _DeleteTimeRange_type_support_ids_t;

static const _DeleteTimeRange_type_support_ids_t _DeleteTimeRange_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _DeleteTimeRange_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _DeleteTimeRange_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _DeleteTimeRange_type_support_symbol_names_t _DeleteTimeRange_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, gantry_lidar_interfaces, srv, DeleteTimeRange)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, gantry_lidar_interfaces, srv, DeleteTimeRange)),
  }
};

typedef struct _DeleteTimeRange_type_support_data_t
{
  void * data[2];
} _DeleteTimeRange_type_support_data_t;

static _DeleteTimeRange_type_support_data_t _DeleteTimeRange_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _DeleteTimeRange_service_typesupport_map = {
  2,
  "gantry_lidar_interfaces",
  &_DeleteTimeRange_service_typesupport_ids.typesupport_identifier[0],
  &_DeleteTimeRange_service_typesupport_symbol_names.symbol_name[0],
  &_DeleteTimeRange_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t DeleteTimeRange_service_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_DeleteTimeRange_service_typesupport_map),
  rosidl_typesupport_c__get_service_typesupport_handle_function,
  &DeleteTimeRange_Request_message_type_support_handle,
  &DeleteTimeRange_Response_message_type_support_handle,
  &DeleteTimeRange_Event_message_type_support_handle,
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_CREATE_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    gantry_lidar_interfaces,
    srv,
    DeleteTimeRange
  ),
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_DESTROY_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    gantry_lidar_interfaces,
    srv,
    DeleteTimeRange
  ),
  &gantry_lidar_interfaces__srv__DeleteTimeRange__get_type_hash,
  &gantry_lidar_interfaces__srv__DeleteTimeRange__get_type_description,
  &gantry_lidar_interfaces__srv__DeleteTimeRange__get_type_description_sources,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace gantry_lidar_interfaces

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_c, gantry_lidar_interfaces, srv, DeleteTimeRange)() {
  return &::gantry_lidar_interfaces::srv::rosidl_typesupport_c::DeleteTimeRange_service_type_support_handle;
}

#ifdef __cplusplus
}
#endif
