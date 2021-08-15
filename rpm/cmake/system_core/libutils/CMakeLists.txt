add_library(libutils SHARED
        FileMap.cpp
        JenkinsHash.cpp
        NativeHandle.cpp
        Printer.cpp
        PropertyMap.cpp
        RefBase.cpp
        SharedBuffer.cpp
        StopWatch.cpp
        String8.cpp
        String16.cpp
        StrongPointer.cpp
        SystemClock.cpp
        Threads.cpp
        Timers.cpp
        Tokenizer.cpp
        Unicode.cpp
        VectorImpl.cpp
        misc.cpp
)

target_include_directories(libutils PUBLIC include)
target_include_directories(libutils PRIVATE ../base/include)
target_include_directories(libutils PRIVATE ../libprocessgroup/include)

# HACK! This package does not have pkg-config!
target_link_libraries(libutils /usr/lib/libsafe_iop.so libcutils liblog)

install(TARGETS libutils
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER)

install(DIRECTORY include/utils DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/linux-hidl)
