add_library(libhidl-gen-host-utils SHARED
    Formatter.cpp
    StringHelper.cpp
)

target_include_directories(libhidl-gen-host-utils PUBLIC include)
target_include_directories(libhidl-gen-host-utils PRIVATE include/hidl-util)
target_link_libraries(libhidl-gen-host-utils libbase)

install(TARGETS libhidl-gen-host-utils
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER)
