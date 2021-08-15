add_library(liblog SHARED
    config_read.cpp
    config_write.cpp
    log_event_list.cpp
    log_event_write.cpp
    logger_lock.cpp
    logger_name.cpp
    logger_read.cpp
    logger_write.cpp
    logprint.cpp
    stderr_write.cpp

    # liblog_host_sources
    fake_log_device.cpp
    fake_writer.cpp
)

target_include_directories(liblog PUBLIC include)
target_include_directories(liblog PRIVATE ../libcutils/include)
target_compile_options(liblog PRIVATE -DFAKE_LOG_DEVICE=1)

install(TARGETS liblog
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER)

install(DIRECTORY include/android include/log DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/linux-hidl)
