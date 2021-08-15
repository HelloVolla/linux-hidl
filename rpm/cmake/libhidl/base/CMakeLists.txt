add_library(libhidlbase SHARED
        HidlInternal.cpp
        HidlSupport.cpp
        Status.cpp
        TaskRunner.cpp
)

target_include_directories(libhidlbase PUBLIC include)
target_link_libraries(libhidlbase libutils libcutils libbase)

install(TARGETS libhidlbase
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER)

install(DIRECTORY include/hidl DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/linux-hidl)
