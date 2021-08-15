add_library(libfmq SHARED
        EventFlag.cpp
        FmqInternal.cpp
)

target_include_directories(libfmq PUBLIC include)
target_link_libraries(libfmq libutils libcutils libbase)

install(TARGETS libfmq
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER)

install(DIRECTORY include/fmq DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/linux-hidl)
