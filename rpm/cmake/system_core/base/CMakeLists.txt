add_library(libbase SHARED
    chrono_utils.cpp
    cmsg.cpp
    file.cpp
    logging.cpp
    mapped_file.cpp
    parsenetaddress.cpp
    properties.cpp
    quick_exit.cpp
    stringprintf.cpp
    strings.cpp
    threads.cpp
    test_utils.cpp
)

target_include_directories(libbase PUBLIC include)
target_link_libraries(libbase liblog bionic_functions)

install(TARGETS libbase
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER)

install(DIRECTORY include/android-base DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/linux-hidl)
