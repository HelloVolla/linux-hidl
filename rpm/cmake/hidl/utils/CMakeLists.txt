add_library(libhidl-gen-utils SHARED
    FQName.cpp
    FqInstance.cpp
)

target_include_directories(libhidl-gen-utils PUBLIC include)
target_include_directories(libhidl-gen-utils PRIVATE include/hidl-util)
target_link_libraries(libhidl-gen-utils libbase)

install(TARGETS libhidl-gen-utils
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER)
