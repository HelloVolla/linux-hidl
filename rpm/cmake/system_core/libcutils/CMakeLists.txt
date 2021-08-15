add_library(libcutils SHARED
    # libcutils_nonwindows_sources
    fs.cpp
    hashmap.cpp
    multiuser.cpp
    socket_inaddr_any_server_unix.cpp
    socket_local_client_unix.cpp
    socket_local_server_unix.cpp
    socket_network_client_unix.cpp
    sockets_unix.cpp
    str_parms.cpp

    # libcutils srcs
    config_utils.cpp
    canned_fs_config.cpp
    iosched_policy.cpp
    load_file.cpp
    native_handle.cpp
    record_stream.cpp
    sockets.cpp
    strdup16to8.cpp
    strdup8to16.cpp
    strlcpy.c
    threads.cpp

    # libcutils android srcs
    android_get_control_file.cpp
    android_reboot.cpp
    ashmem-dev.cpp
    fs_config.cpp
    klog.cpp
    partition_utils.cpp
    properties.cpp
    qtaguid.cpp
    trace-dev.cpp
    uevent.cpp
)

target_include_directories(libcutils PUBLIC include)
target_include_directories(libcutils PRIVATE ../libutils/include)
target_link_libraries(libcutils libbase liblog bionic_functions)

install(TARGETS libcutils
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER)

install(DIRECTORY include/cutils DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/linux-hidl)
